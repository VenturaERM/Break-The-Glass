# VENTURA ERM
VENTURA ERM is a tool designed to automate the collection, storage, and analysis of AWS CloudTrail event logs. It enables users to download CloudTrail event files from multiple AWS regions, compress them, and generate security hashes for integrity checks.

## Prerequisites
Python 3.x

AWS SDK for Python (Boto3)

Configured AWS CLI access with appropriate permissions


## Installation
Clone the repository: git clone https://github.com/VenturaERM/Break-The-Glass

Install the necessary dependencies: pip install boto3 requests

## Usage
To use VENTURA ERM, follow these steps:

Configure your AWS CLI environment with your credentials and desired region.

Run the script: python [Break-The-Glass.py](https://github.com/VenturaERM/Break-The-Glass/blob/main/break_the_glass.py)

CloudTrail files will be automatically downloaded, compressed, and their integrity verified.

## Contributions
Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch: git checkout -b my-new-feature

Make your changes and commit: git commit -am 'Add some feature'

Push to the branch: git push origin my-new-feature

Submit a pull request.

## License
This project is licensed under [MIT](https://github.com/VenturaERM/Break-The-Glass/blob/main/LICENSE). 
See the LICENSE file for more details.

## Contact
For contact, please send an email to [contato@venturaerm.com](https://venturaerm.com/contact_us).
