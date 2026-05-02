# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys

from typing import List

from solution.consumer_sol import mqConsumer  # pylint: disable=import-error

def main(sectors: List[str], queueName: str) -> None:
    
    # Logic to create BKs from tickers and multiple sectors.
    bindingKeys = [f"#.{sector}" for sector in sectors]
    
    # Create consumer that's suscribed to multiple sectors.
    consumer = mqConsumer(binding_keys=bindingKeys,exchange_name="Tech Lab Topic Exchange",queue_name=queueName)   

    consumer.startConsuming()

if __name__ == "__main__":
    sector = None
    queue  = None

    if len(sys.argv) < 3:
        raise RuntimeError("Must have at least 2 inputs on command line.")
    else:
        sector = sys.argv[1:-1]
        queue  = sys.argv[-1]

    sys.exit(main(sector,queue))
