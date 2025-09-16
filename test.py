import asyncio
import logging

from pyenjoy import AsyncEnjoyClient
from pyenjoy.definition import register_names as rn
import pprint

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

async def main():

    try:
            client = AsyncEnjoyClient(ip="192.168.150.100")
            if not await client.connect():
                raise ConnectionError("Failed to connect to inverter")
            logger.info("Successfully connected to inverter")

            try:
                inverter = {
                    rn.serial_number_n: await client.get(rn.serial_number_n)
                }
                pprint.pprint(inverter)

                await client.close()
            except Exception as e:
                await client.close()
                print(str(e))


    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise e
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())