"""The implementation of the Application class"""
import json

from common.app.app_base import ApplicationBase

from nats_messenger import Messenger

# from mpa import MessageConsumerActor
from rpc import RPCServer


class Application(ApplicationBase):
    """
    The Application class
    """

    rpc_server = None

    async def start(self):
        """Starts the application, and sets up the internal modules and services"""
        self.logger.info("app starts")
        self.logger.info(self.config)

        # Setup RPC Server
        self.rpc_server = RPCServer(
            Messenger(
                self.config.MESSENGER_URL,
                self.logger,
                name=self.config.MESSENGER_CLIENT_ID,
            )
        )

        async def service_fun(payload: bytes, headers: dict) -> bytes:
            # payload_json = json.loads(payload.decode("utf8"))
            self.logger.debug(
                f"Service function is called with message payload: '{payload}', headers: {headers}"
            )
            response_json = {
                "status": 200,
                "headers": {
                    "content-type": "application/json",
                },
                "body": [
                    {
                        "id": "luke-skywalker",
                        "familyName": "Skywalker",
                        "givenName": "Luke",
                    }
                ],
            }
            response = json.dumps(response_json).encode("utf8")
            msg_response_headers = {
                "content-type": "application/json",
                "message-type": "rpc/response",
            }
            return response, msg_response_headers

        try:
            # Open RPC servers
            await self.rpc_server.open()
            self.logger.debug("RPC server start listening")
            await self.rpc_server.listen("easer.get_/persons", service_fun=service_fun)

        except Exception as exception:
            self.logger.error(
                f"Exception happened at channel openings: {exception}", exc_info=True
            )
            raise exception

    async def stop(self):
        """Shuts down the application"""
        self.logger.info("app shuts down")

        # Close the RPC servers
        self.rpc_server.close()
