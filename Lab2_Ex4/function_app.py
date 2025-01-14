import azure.functions as func
import logging
import math

app = func.FunctionApp()  

@app.route(route="numericalintegral/{lower}/{upper}", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def numerical_integral(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing numerical integral function.")

    try:
        lower = float(req.route_params.get("lower"))
        upper = float(req.route_params.get("upper"))

        def numerical_integration(lower, upper, n):
            dx = (upper - lower) / n
            integral = 0.0
            for i in range(n):
                x = lower + (i + 0.5) * dx
                integral += abs(math.sin(x)) * dx
            return integral

        n_values = [10, 100, 1000, 10000, 100000, 1000000]
        results = [{"n": n, "integral": round(numerical_integration(lower, upper, n), 10)} for n in n_values]

        return func.HttpResponse(
            body=str(results),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return func.HttpResponse(
            f"Invalid request: {e}",
            status_code=400,
        )
