from celery import Celery
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time

celery = Celery(__name__)

@celery.task
def get_predicted_price(house_price_df, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition):
    X = house_price_df[
        [
            "bedrooms",
            "bathrooms",
            "sqft_living",
            "sqft_lot",
            "floors",
            "waterfront",
            "view",
            "condition",
        ]
    ]
    y = house_price_df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predicted_price = model.predict(
        [
            [
                bedrooms,
                bathrooms,
                sqft_living,
                sqft_lot,
                floors,
                waterfront,
                view,
                condition,
            ]
        ]
    )[0]
    time.sleep(10)
    return predicted_price