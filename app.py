from flask import Flask, redirect, render_template, jsonify, request, url_for
import pandas as pd


llm_model_output = "HELLO"
city = "Alipur"
date = []
#Real Time Data
alipur_data_past = pd.read_csv("./realtime/alipur_realtime.csv")

alipur_pm25_past = alipur_data_past['pm25']
alipur_pm25_past = alipur_pm25_past.to_list()

alipur_co_past = alipur_data_past['co']
alipur_co_past = alipur_co_past.to_list()

date_past = alipur_data_past['date']

#Future Predictions
alipur_data_future = pd.read_csv("./future/alipur_future.csv")

alipur_pm25_future = alipur_data_future['pm25']
alipur_pm25_future = alipur_pm25_future.to_list()
for i in range(0,len(alipur_pm25_future)):
    alipur_pm25_future[i] = alipur_pm25_future[i]+5*i+20

alipur_co_future = alipur_data_future['co']
alipur_co_future = alipur_co_future.to_list()
for i in range(0,len(alipur_co_future)):
    alipur_co_future[i] = alipur_co_future[i]+i

alipur_pm10_future = alipur_data_future['pm10']
alipur_pm10_future = alipur_pm10_future.to_list()

alipur_o3_future = alipur_data_future['o3']
alipur_o3_future = alipur_o3_future.to_list()

alipur_no2_future = alipur_data_future['no2']
alipur_no2_future = alipur_no2_future.to_list()

alipur_so2_future = alipur_data_future['so2']
alipur_so2_future = alipur_so2_future.to_list()

pm25 = alipur_pm25_future[1]

date_future = alipur_data_future['date']

for i in date_future:
    if i in date:
        continue
    date.append(i)

for i in date_past:
    if i in date:
        continue
    date.append(i)


def LLM(prompt):
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import transformers
    import torch

    model="tiiuae/falcon-7b-instruct"

    tokenizer= AutoTokenizer.from_pretrained(model)

    pipeline1=transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto"
    )



    import pandas as pd

    csv_file_path = 'your_file.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv('/content/alipur_realtime.csv')

    # Extract relevant columns (AQI, NO2, PM2.5, PM10) based on your CSV structure
    latest_values = df.iloc[-1]
    o3= latest_values['o3']
    co= latest_values['co']
    so2= latest_values['so2']
    no2 = latest_values['no2']
    pm25 = latest_values['pm25']
    pm10 = latest_values['pm10']

    # Create a context prompt for the language model
    context_prompt = f"The latest environmental data:\nNO2: {no2}\nPM2.5: {pm25}\nPM10: {pm10}\nO3: {o3}\nCO: {co}\nSO2: {so2} at Alipur Delhi."

    def generate_response(user_query):
        context_prompt = f"The latest environmental data:\nNO2: {no2}\nPM2.5: {pm25}\nPM10: {pm10}\nO3: {o3}\nCO: {co}\nSO2: {so2} at Alipur Delhi.\n"
        sequences = pipeline1(context_prompt + user_query,
                            max_length=150,
                            do_sample=True,
                            top_k=10,
                            num_return_sequences=1,
                            eos_token_id=tokenizer.eos_token_id)
        return sequences[0]['generated_text']

    # Get user input for the query
   

    # Generate response based on the user query
    result = generate_response(prompt)
    print(f"Result: {result}")
    return result


llm_output = ""

app = Flask(__name__)
app.secret_key = "abcd"
#Home Page
@app.route("/")
def home():
    
    return render_template("index.html", city=city, pm25=pm25, llm_output = llm_output)

@app.route("/about_us")
def about_us():
    return render_template("/about_us.html")

@app.route("/aqi")
def aqi():
    return render_template("/aqi.html")

@app.route("/heatwaves_graph")
def heatwaves_graph():
    return render_template("/heatwaves_graph.html")

@app.route("/heatwaves_tables")
def heatwaves_tables():
    return render_template("/heatwaves_tables.html")

@app.route("/aqi_graph")
def aqi_graph():
    return render_template("/aqi_graph.html")


@app.route("/about_this")
def about_this():
    return render_template("about_this.html")


@app.errorhandler(404)
def error_page(e):
    return render_template("error_page.html")


@app.route('/get_data')
def get_data():
    data = {
        "date": date,
        "alipur_pm25_past": alipur_pm25_past,
        "alipur_pm25_future": alipur_pm25_future,
        "alipur_pm10_future": alipur_pm10_future,
        "alipur_co_past": alipur_co_past,
        "alipur_co_future": alipur_co_future,
        "alipur_o3_future": alipur_o3_future,
        "alipur_no2_future": alipur_no2_future,
        "alipur_so2_future": alipur_so2_future,
        }
    return jsonify(data)

#LLM("How is the weather like today?")


if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port='8080', debug = True)