
# MLOps

The project was made by : KHALI Mohammed Adam ,LAABYDY Mohamed :)

![225813708-98b745f2-7d22-48cf-9150-083f1b00d6c9](https://github.com/Adamkhali0/TP-TDLOG/assets/118823327/2b4d03ca-0eb6-4e42-8f5b-d188fa1f5bdd)
# TWITTER STOCK MARKET ![241765460-cc4fe88c-7f7a-41d8-b449-34b7a178c1c6](https://github.com/Adamkhali0/TP-TDLOG/assets/118823327/422c48e3-cc6c-4229-a29f-5ccdcfcbb916)

Twitter was founded in 2006 and went public in 2013. Since the inception of Twitter, the year 2022 has been a memorable event for the platform. When Elon Musk took control of Twitter, it was delisted from the New York Stock Exchange. As 2022 has been so eventful for Twitter, let's analyze the complete timeline of Twitter on the stock market from 2013 to 2022.

Twitter is one of the popular social media applications where people share their thoughts in a limited number of words. Twitter is popular but not on the stock market.

The data includes:

Date

The opening price of the day

The highest price of the day

The lowest price of the day

The closing price of the day

The adjusted closing price of the day

The total number of shares traded in the day (volume)

The goal of this project is to analyze the performance of Twitter on the stock market during the period from 2013 to 2022 and predict by highlighting the key events of this period.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creating Docker Image for the API Predicting Stock Value at the End of the Day
1. Open a terminal and navigate to your project folder.
2. Execute the following command to build the Docker image:
    ```bash
    docker build -t api_TSM.py .
    ```

## Starting the Application in Development Mode

- For easy debugging, it is recommended to start the application via your IDE (PyCharm or VSCode).
## Starting Prometheus and Grafana

1. Execute the following command to start Prometheus and Grafana:
    ```bash
    docker compose up -d
    ```

2. This configuration is ready to work with the application launched in development mode.

## Accessing Prometheus and Grafana

- Open a browser and access Prometheus on port 9090.
- For Grafana, access port 3000. Use "admin" as the username and "grafana" as the password.



# Access to Containers and Ports

Now, you have access to these three containers and their respective ports:

- **Prometheus:** [http://localhost:9090/](http://localhost:9090/)
- **Grafana:** [http://localhost:3000/](http://localhost:3000/)
- **FastAPI:** [http://localhost:8000/](http://localhost:8000/)

## Credentials:

- **Nom d'utilisateur :** admin
- **Mot de passe :** admin


