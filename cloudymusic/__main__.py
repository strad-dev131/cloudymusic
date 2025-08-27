#  Copyright (c) 2025 strad-dev131
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the cloudymusic project. All rights reserved where applicable.

from cloudymusic import client


def main() -> None:
    client.logger.info("Starting cloudymusic...")
    client.run()


if __name__ == "__main__":
    main()
