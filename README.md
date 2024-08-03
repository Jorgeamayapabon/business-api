
# Business API Project

This is an API for a business that wants to register users, customers and sales. Here you will find out how to get it up and running.

In this project the event architecture and rest api were implemented
## Authors

- [Jorge Amaya Pabon](https://github.com/Jorgeamayapabon)


## Installation

1️⃣ Clone repo with git

```bash
  git clone https://github.com/Jorgeamayapabon/business-api.git
```

2️⃣ Create a virtual environment in python, activate it and install dependencies

```bash
  py -m venv venv
```
```bash
.\venv\Scripts\activate
```
```bash
  pip install -r requirements.txt
```

3️⃣ Compress the directories business_api > business-api.zip, event_processor > event-processor.zip, sales_processor > sales-processor.zip. Here's how to do it on Windows

```bash
  Compress-Archive -Path .\business_api\*.py -DestinationPath .\infrastructure\business-api.zip -f
```
```bash
  Compress-Archive -Path .\sales_processor\*.py -DestinationPath .\infrastructure\sales-processor.zip -f
```
```bash
  Compress-Archive -Path .\event_processor\*.py -DestinationPath .\infrastructure\event-processor.zip -f
```

4️⃣ Create the layer for the lambdas and compress it. This is how it is done on Windows.
```bash
  pip install -r .\requirements.txt --platform=manylinux2014_x86_64 --only-binary=:all: --target python/lib/python3.10/site-packages
```
```bash
  Compress-Archive -Path .\python -DestinationPath .\infrastructure\business-api-layer.zip -f
```

5️⃣ Inside the infrastructure directory. Run the following commands.

```bash
  cd .\infrastructure\
```
```bash
  terraform init
```
```bash
  terraform apply
```
Then it asks you for confirmation
```bash
  yes
```
6️⃣ All that's left to do is import the collection into Postman and that's it. Great! Now you can use it.


## Feedback

If you have any comments, please contact me at jeap1723@gmail.com
