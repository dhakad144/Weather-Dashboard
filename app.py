from flask import *
import requests
import datetime

timestamp = 1726636384

dt_object = datetime.datetime.utcfromtimestamp(timestamp)

print(dt_object.strftime("%Y-%m-%d %H:%M:%S"))
apikey = '9b84156024a1157f9ceaf83477c026d7'

class Weather:

    def check(self,item):
        if item:
            return f',{item}'
        return ''
    
    def presencechecker(self,a,value):
        try:
            return a[value]
        except:
            return 'not avaliable'

    
    def getweatherdata(self,city_name,country_code=None):
        api = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}{self.check(country_code)}&appid={apikey}'
        try:
            response = requests.get(api)
            data = response.json()
            # print(data)
            lat = data[0]['lat']
            lon = data[0]['lon']
        except requests.exceptions.RequestException as e:
            return f'error: {e}'
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={apikey}')
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return f'error: {e}'



app = Flask(__name__)
obj = Weather()
@app.route('/')
def home():
    # return render_template('index.html',)
        data = obj.getweatherdata(city_name='indore',country_code='IN')
        
        dt  = obj.presencechecker( data,'dt')
        dt_object = datetime.datetime.utcfromtimestamp(dt)
        dt = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        sunrise  = obj.presencechecker( data['sys'],'sunrise')
        dt_object = datetime.datetime.utcfromtimestamp(sunrise)
        sunrise = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        sunset  = obj.presencechecker( data['sys'],'sunset')
        dt_object = datetime.datetime.utcfromtimestamp(sunset)
        sunset = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        return render_template('index.html',
                            longitude = obj.presencechecker( data['coord'],'lon'),
                            latitude = obj.presencechecker( data['coord'],'lat'),
                            main = obj.presencechecker( data['weather'][0],'main').upper(),
                            description = obj.presencechecker( data['weather'][0],'description'),
                            icon = obj.presencechecker( data['weather'][0],'icon'),
                            temp  = obj.presencechecker( data['main'],'temp'),
                            feels_like  = obj.presencechecker( data['main'],'feels_like'),
                            temp_min  = obj.presencechecker( data['main'],'temp_min'),
                            temp_max  = obj.presencechecker( data['main'],'temp_max'),
                            pressure  = obj.presencechecker( data['main'],'pressure'),
                            humidity  = obj.presencechecker( data['main'],'humidity'),
                            sea_level  = obj.presencechecker( data['main'],'sea_level'),
                            grnd_level  = obj.presencechecker( data['main'],'grnd_level'),
                            visibility  = obj.presencechecker( data,'visibility'),
                            speed  = obj.presencechecker( data['wind'],'speed'),
                            deg  = obj.presencechecker( data['wind'],'deg'),
                            gust  = obj.presencechecker( data['wind'],'gust'),
                            rain  = obj.presencechecker( obj.presencechecker(data,'rain'),'1h'),
                            clouds  = obj.presencechecker( data['clouds'],'all'),
                            country  = obj.presencechecker( data['sys'],'country'),
                            dt  = dt,
                            sunrise  = sunrise,
                            sunset  = sunset,
                            cityname  = obj.presencechecker( data,'name').upper(),
                               )

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        city = request.form.get('city_name')
        country_code = request.form.get('city_name')
        
        data = obj.getweatherdata(city_name=city,country_code=country_code)
        
        dt  = obj.presencechecker( data,'dt')
        dt_object = datetime.datetime.utcfromtimestamp(dt)
        dt = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        sunrise  = obj.presencechecker( data['sys'],'sunrise')
        dt_object = datetime.datetime.utcfromtimestamp(sunrise)
        sunrise = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        sunset  = obj.presencechecker( data['sys'],'sunset')
        dt_object = datetime.datetime.utcfromtimestamp(sunset)
        sunset = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        return render_template('index.html',
                            longitude = obj.presencechecker( data['coord'],'lon'),
                            latitude = obj.presencechecker( data['coord'],'lat'),
                            main = obj.presencechecker( data['weather'][0],'main').upper(),
                            description = obj.presencechecker( data['weather'][0],'description'),
                            icon = obj.presencechecker( data['weather'][0],'icon'),
                            temp  = obj.presencechecker( data['main'],'temp'),
                            feels_like  = obj.presencechecker( data['main'],'feels_like'),
                            temp_min  = obj.presencechecker( data['main'],'temp_min'),
                            temp_max  = obj.presencechecker( data['main'],'temp_max'),
                            pressure  = obj.presencechecker( data['main'],'pressure'),
                            humidity  = obj.presencechecker( data['main'],'humidity'),
                            sea_level  = obj.presencechecker( data['main'],'sea_level'),
                            grnd_level  = obj.presencechecker( data['main'],'grnd_level'),
                            visibility  = obj.presencechecker( data,'visibility'),
                            speed  = obj.presencechecker( data['wind'],'speed'),
                            deg  = obj.presencechecker( data['wind'],'deg'),
                            gust  = obj.presencechecker( data['wind'],'gust'),
                            rain  = obj.presencechecker( obj.presencechecker(data,'rain'),'1h'),
                            clouds  = obj.presencechecker( data['clouds'],'all'),
                            country  = obj.presencechecker( data['sys'],'country'),
                            dt  = dt,
                            sunrise  = sunrise,
                            sunset  = sunset,
                            cityname  = obj.presencechecker( data,'name').upper(),
                               )
    

    




if __name__ == '__main__':
    app.run(debug=True)
                            #    longitude=data['coord']['lon'],
                            #    latitude=data['coord']['lat'],
                            #    main=data['weather'][0]['main'],
                            #    description=data['weather'][0]['description'],
                            #    icon=data['weather'][0]['icon'],
                            #    temp = data['main']['temp'],
                            #    feels_like = data['main']['feels_like'],
                            #    temp_min = data['main']['temp_min'],
                            #    temp_max = data['main']['temp_max'],
                            #    pressure = data['main']['pressure'],
                            #    humidity = data['main']['humidity'],
                            #    sea_level = data['main']['sea_level'],
                            #    grnd_level = data['main']['grnd_level'],
                            #    visibility = data['visibility'],
                            #    speed = data['wind']['speed'],
                            #    deg = data['wind']['deg'],
                            # #    gust = data['wind']['gust'],
                            # #    rain = data['rain']['1h'],
                            #    clouds = data['clouds']['all'],
                            #    dt = data['dt'],
                            #    country = data['sys']['country'],
                            #    sunrise = data['sys']['sunrise'],
                            #    sunset = data['sys']['sunset'],
                            #    cityname = data['name']