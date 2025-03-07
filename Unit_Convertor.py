import streamlit.components.v1 as components
import streamlit as st 

st.header('**Digital Unit Convertor :**')
options=["Length",'Mass',"Temperature","Speed","Volume","Area","Time","Frequency","Angle","Force","Pressure","Energy",'Power','Electric Current','Voltage','Resistance','Digital Storage',"Fuel Consumption",]

cat=st.selectbox("Select an Option:",options)
st.write(f'***:blue[You Selected "___{cat}___"]***')
def length():
        length_mult= {
        "Meter":1,
        "Kilometer":0.001,
        "Miles":0.000621371,
        "Decimeter":10,
        "Centimeter":100,
        "Milimeter":1000,
        "Micron":1000000,
        "Nanometer":1000000000,
        "Picometer":1000000000000,
        "Femtometer":1000000000000000,
        "Attometer":1000000000000000000,
        "Zeptometer":1000000000000000000,
        "Yocktometer":1000000000000000000,
        'Dekameter':0.1,
        'Hectometer':0.01,
        'Megameter':0.000001,
        'Gigameter':0.000000001,
        'Terameter':0.000000000001,
        'Petameter':0.000000000000001,
        'Exameter':0.000000000000000001,
        'Zettameter':0.000000000000000000001,
        'Yottameter':0.000000000000000000000001,
        'Yard':1.09361,
        'Foot':3.28084,
        'Inch':39.3701,
        'Mil':39370.1,
        'Nautical Mile':0.000539957,
        'Li':0.002,
        'Half Marathon':0.000047,
        'Marathon':0.000023,
        'Parsec':3.24078e-17,
        'Milliparsec':3.24078e-14,
        'Nanoparsec':3.24078e-8,
        'Picoparsec':3.24078e-5,
        'Kiloparsec':3.24078e-20,
        'Megaparsec':3.24078e-23,
        'Gigaparsec':3.24078e-26,
        'Teraparsec':3.24078e-29,
        'Astronomical Unit':6.68459e-12,
        'Light Year':1.057e-16,
        'League':0.0002071237,
        'Chain':0.0497097,
        'Furlong':0.00497097,
        'Mega Furlong':4.97097e-9,
        'Rod':0.198838,
        'Fathom':0.546807,
        'Cubit':2.18723,
        'Beard Second':5.066e11,
        'Angstrom':1e10,
    }
        length_factors=list(length_mult.keys())
                        
        inp=st.selectbox("From :",length_factors)
        opt=st.selectbox("To :",length_factors)
        val=st.number_input(f"Enter The Value Of Length In :blue-background[{inp}] To Convert Into :blue-background[{opt}] :", value=0.0, step=0.01)

        met=val/length_mult[inp]
        result=met*length_mult[opt]
        st.subheader("Results:")
        st.markdown(f'***:blue-background[{val} {inp} = :green-background[{result:.2f} {opt}]]***')

def temp():
    temperatures =['Fahrenheit','Kelvin','Rankine','Celsius']
    inp_temp=st.selectbox("From:",temperatures)
    opt_temp=st.selectbox("To:",temperatures)
    temperature=st.number_input(f"Enter The Temperature In :blue-background[{inp_temp}] To Convert Into :blue-background[{opt_temp}] :", value=0.0, step=0.01)
    st.subheader("Results:")
    
        
    if inp_temp == "Fahrenheit":
        celsius=(temperature - 32) * 0.5555555555555556
    elif inp_temp=="Kelvin":
        celsius=temperature -273.15
    elif inp_temp == "Rankine":
        celsius=(temperature -491.67) * 0.5555555555555556
    else:
         celsius=temperature

    if opt_temp=="Fahrenheit":
        celsius_fahrenheit =(celsius * 1.8 ) + 32
        st.markdown(f'***:blue-background[{temperature} {inp_temp}  =   :green-background[{celsius_fahrenheit:.2f} {opt_temp}]]***')
    elif opt_temp == "Kelvin":
        celsius_kelvin=celsius+273.15
        st.markdown(f'***:blue-background[{temperature} {inp_temp}  =   :green-background[{celsius_kelvin:.2f} {opt_temp}]]***')
    elif opt_temp == "Rankine":
        celsius_rankine= (celsius +273.15) * 1.8
        st.markdown(f'***:blue-background[{temperature} {inp_temp}  =   :green-background[{celsius_rankine:.2f} {opt_temp}]]***')
    else:
           st.markdown(f'***:blue-background[{temperature} {inp_temp}  =   :green-background[{celsius:} {opt_temp}]]***')
        

    

def area():
    area_mult={
        "Sq. Meter":1,
        "Sq. Kilometer":0.000001,
        "Hectare":0.0001,
        "Are":0.01,
        "Square Decimeter":100,
        "Square Centimeter":10000,
        "Square Millimeter":1000000,
        "Sq. Mile":3.8610e-7,
        "Acre":0.00024711,
        "Sq. Yard":1.19599005,
        " Sq. Foot":10.7639104,
        "Sq. Inch":1550.0031,
        "Square Rod":0.039536861097273,
        "Rood":9.884215215699621e-4,
        "Barn":1.0000e+28,
        }
    area_factors= list(area_mult.keys())
    inp_area=st.selectbox("From :",area_factors)
    opt_area=st.selectbox("To :",area_factors)
    area=st.number_input(f"Enter The Value Of Area In :blue-background[{inp_area}] To Convert Into :blue-background[{opt_area}] :", value=0.0, step=0.01)
    st.subheader("Results:")
    sq_meter=area/area_mult[inp_area]
    area_result=sq_meter*area_mult[opt_area]
    st.markdown(f'***:blue-background[{area} {inp_area} = :green-background[{area_result} {opt_area}]]***')


def fuelconsumption():
    fuel_mult={
        "Km/liter":1,
        "MPG (US)":2.35214584,
        "MPG (Imp.)":2.82481061,
        "Liter/100km":100,
        }
    fuel_factors=["MPG (US)","Km/liter","MPG (Imp.)","Liter/100km"]
    inp_fuel=st.selectbox("From :",fuel_factors)
    opt_fuel=st.selectbox("To :",fuel_factors)
    fuel=st.number_input(f"Enter The Value Of Fuel In :blue-background[{inp_fuel}] To Convert Into :blue-background[{opt_fuel}] :", value=0.0, step=0.01)
    km_l=fuel/fuel_mult[inp_fuel]
    converted_fuel=km_l*fuel_mult[opt_fuel]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{fuel} {inp_fuel} = :green-background[{converted_fuel:.2f} {opt_fuel}]]***')

def digital_storage():
    storage_mult={
          "Bit":1,
          "Nibble" : 0.25,
          "Byte" : 0.125,
          "Kilobit" : 0.001,
          "Kibibit" : 0.00097656,
          "Kilobyte" : 0.000125,
          "Kibibyte" : 0.00012207,
          "Megabit" : 0.000001,
          "Mebibit" : 9.5367e-7,
          "Megabyte" : 1.2500e-7,
          "Mebibyte" : 1.1921e-7,
          "Gigabit" : 1.0000e-9,
          "Gibibit" : 9.3132e-10,
          "Gigabyte" :1.2500e-10,
          "Gibibyte" : 1.1642e-10,
          "Terabit" :1.0000e-12,
          "Tebibit":9.0949E-13,
          "Terabyte" :1.2500e-13,
          "Tebibyte" :1.1369e-13,
          "Petabit" :1.0000e-15,
          "Pebibit" :8.8818e-16,
          "Petabyte" : 1.2500e-16,
          "Pebibyte" : 1.1102e-16,
          "Exabit" : 1.0000e-18,
          "Exbibit" : 8.6736e-19,
          "Exabyte" : 1.2500e-19,
          "Exbibyte":1.0842e-19,
          "Zettabit" : 1.0000e-21,
          "Zebibit" : 8.4703e-22,
          "Zettabyte" :1.2500e-22,
          "Zebibyte" :1.0588e-22,
          "Yottabit" : 1.0000e-24,
          "Yobibit" :8.2718e-25,
          "Yottabyte" :1.2500e-25,
          "Yobibyte" : 1.0340e-25,}
    
    storage_factors=list(storage_mult.keys())


    inp_str=st.selectbox("From :",storage_factors)
    opt_str=st.selectbox("To :",storage_factors)
    storage_value=st.number_input(f"Enter The Value Of Storage In :blue-background[{inp_str}] To Convert Into :blue-background[{opt_str}] :", value=0.0, step=0.01)    
    bit=storage_value/storage_mult[inp_str]
    result=bit*storage_mult[opt_str]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{storage_value} {inp_str} = :green-background[{result:.2f} {opt_str}]]***') 


def resistance():
    resistance_mult={
        "Ohm":1,
        "Micro Ohm":1000000,
        "Mili Ohm":1000,
        "Kilo Ohm":0.001,
        "Mega Ohm":0.000001,
        }

    resistance_factors=list(resistance_mult.keys())
    inp_resistance=st.selectbox("From :",resistance_factors)
    opt_resistance=st.selectbox("To :",resistance_factors)
    resistance_value=st.number_input(f"Enter The Value Of Resistance In :blue-background[{inp_resistance}] To Convert Into :blue-background[{opt_resistance}] :", value=0.0, step=0.01)    
    ohm=resistance_value/resistance_mult[inp_resistance]
    result=ohm*resistance_mult[opt_resistance]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{resistance_value} {inp_resistance} = :green-background[{result:.2f} {opt_resistance}]]***') 

def voltage():
    voltage_mult={
        'Volt':1,
        'Microvolt':1000000,
        'Millivolt':1000,
        'Kilovolt':0.001,
        'Megavolt':0.000001,
        'Gigavolt':1.0000e-9,
        'Teravolt':1.0000e-12,
        'Petavolt':1.0000e-15,
        'Exavolt':1.0000e-18,
        }
    voltage_factors =list(voltage_mult.keys())

    inp_voltage=st.selectbox("From :",voltage_factors)
    opt_voltage=st.selectbox("To :",voltage_factors)
    voltage_value=st.number_input(f"Enter The Value Of Voltage In :blue-background[{inp_voltage}] To Convert Into :blue-background[{opt_voltage}] :", value=0.0, step=0.01)    
    volt=voltage_value/voltage_mult[inp_voltage]
    result=volt*voltage_mult[opt_voltage]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{voltage_value} {inp_voltage} = :green-background[{result:.2f} {opt_voltage}]]***') 

def electric_current():
    current_mult={
        'Ampere ':1,
        'Microampere':1000000,
        'Milliampere':1000,
        'Kiloampere ':0.001,
        'Megaampere ':0.000001,
        'Gigaampere ':1.0000e-9,
        'Teraampere ':1.0000e-12,
        'Petaampere ':1.0000e-15,
        'Exaampere':1.0000e-18,
        }
    current_factors=list(current_mult.keys())

    inp_current=st.selectbox("From :",current_factors)
    opt_current=st.selectbox("To :",current_factors)
    current_value=st.number_input(f"Enter The Value Of Current In :blue-background[{inp_current}] To Convert Into :blue-background[{opt_current}] :", value=0.0, step=0.01)
    ampere=current_value/current_mult[inp_current]
    result=ampere*current_mult[opt_current]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{current_value} {inp_current} = :green-background[{result:.2f} {opt_current}]]***') 

def power():
    power_mult={
        "Watt":1,
        "Kilowatt":0.001,
        "Megawatt":0.000001,
        "Gigawatt":1.0000e-9,
        "Terawatt":1.0000e-12,
        "Petawatt":1.0000e-15,
        "Exawatt":1.0000e-18,
        "Horsepower":0.00134102,
        }
    power_factors=list(power_mult.keys())

    inp_power=st.selectbox("From :",power_factors)
    opt_power=st.selectbox("To :",power_factors)
    power_value=st.number_input(f"Enter The Value Of Power In :blue-background[{inp_power}] To Convert Into :blue-background[{opt_power}] :", value=0.0, step=0.01)
    watt=power_value/power_mult[inp_power]
    result=watt*power_mult[opt_power]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{power_value} {inp_power} = :green-background[{result:.2f} {opt_power}]]***') 

def mass():
    mass_mult={
        'Kilogram':1,
         'Gram':1000,
         'Decigram':10000,
         'Centigram':100000,
         'Milligram':1000000,
         'Microgram':1.0000e+9,
         'Nanogram':1.0000e+12,
         'Picogram':1.0000e+15,
         'Femtogram':1.0000e+18,
         'Dekagram':100,
         'Hectogram':10,
         'Megagram':0.001,
         'Metric ton':0.001,
         'Long ton':0.00098421,
         'Short ton':0.00110231,
         'Imperial ton':0.00098421,
         'Metric quintal':0.01,
         'US quintal':0.02204623,
         'French quintal':0.00671366,
         'Stone':0.15747304,
        'Pound':2.20462262,
         'Ounce ':35.273962,
        'Troy ounce':32.1507466,
        'Slug ':0.06852177,
        'Tola ':85.7353242,
        'Dram ':564.38339,
        'Carat ':5000,
        'Grain ':15432.3584,
        'Atomic Mass Unit' :6.0221e+26,

        }
    
    mass_factors=list(mass_mult.keys())

    inp_mass=st.selectbox("From :",mass_factors)
    opt_mass=st.selectbox("To :",mass_factors)
    mass_value=st.number_input(f"Enter The Amount Of Mass In :blue-background[{inp_mass}] To Convert Into :blue-background[{opt_mass}] :", value=0.0, step=0.01)
    kl_gram=mass_value/mass_mult[inp_mass]
    result=kl_gram*mass_mult[opt_mass]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{mass_value} {inp_mass} = :green-background[{result:.2f} {opt_mass}]]***') 

def speed():
    speed_mult={
        "Meter/Second":1,
        "Mile/Hour":2.23693629,
        "Kilometer/Hour":3.6,
        "Foot/Second":3.2808399,
        "Knot":1.94384449,
        "Mach":0.00291545,
        }
    speed_factors=list(speed_mult.keys())
    inp_speed=st.selectbox("From :",speed_factors)
    opt_speed=st.selectbox("To :",speed_factors)
    speed_value=st.number_input(f"Enter The Amount Of Speed In :blue-background[{inp_speed}] To Convert Into :blue-background[{opt_speed}] :", value=0.0, step=0.01)
    m_s=speed_value/speed_mult[inp_speed]
    result=m_s*speed_mult[opt_speed]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{speed_value} {inp_speed} = :green-background[{result:.2f} {opt_speed}]]***') 


def frequency():
    frequency_mult={
        "Hertz":1,
        "MicroHertz":1000000,
        "MiliHertz":1000,
        "KiloHertz":0.001,
        "MegaHertz":0.000001,
        "GigaHertz":1.0000e-9,
        "TeraHertz":1.0000e-12,
        "PetaHertz":1.0000e-15,
        "ExaHertz":1.0000e-18,
        }
    
    frequency_factors=list(frequency_mult.keys())

    inp_frequency=st.selectbox("From :",frequency_factors)
    opt_frequency=st.selectbox("To :",frequency_factors)
    frequency_value=st.number_input(f"Enter The Amount Of Frequency In :blue-background[{inp_frequency}] To Convert Into :blue-background[{opt_frequency}] :", value=0.0, step=0.01)
    hertz=frequency_value/frequency_mult[inp_frequency]
    result=hertz*frequency_mult[opt_frequency]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{frequency_value} {inp_frequency} = :green-background[{result:.2f} {opt_frequency}]]***') 


def angle():
    angle_mult={
        "Radian":1,
        "Degree":57.2957795,
        "Miliradian":1000,
        "Microradian":0.001,
        "Gradiun":0.000001,
        "Revolution":1.0000e-9,
        "Arc Minute":1.0000e-12,
        "Arc Second":1.0000e-15,
        "Miliarcsecond":1.0000e-18,
        "Microarcsecond":1.0000e-18,
        }
    
    angle_factors=list(angle_mult.keys())

    inp_angle=st.selectbox("From :",angle_factors)
    opt_angle=st.selectbox("To :",angle_factors)
    angle_value=st.number_input(f"Enter Angle In :blue-background[{inp_angle}] To Convert Into :blue-background[{opt_angle}] :", value=0.0, step=0.01)
    hertz=angle_value/angle_mult[inp_angle]
    result=hertz*angle_mult[opt_angle]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{angle_value} {inp_angle} = :green-background[{result:.2f} {opt_angle}]]***') 

def force():

    force_mult= {
    "Newton": 1,
    "Kilonewton":0.001,
    "Dyne":100000,
    "Gram-force": 101.971621,
    "Ounce-force":3.59694309,
    "Pound-force":0.22480894,
    "Kilogram-force":0.10197162,
    "Kip-force":0.00022481,
    "Metric ton-force": 0.00010197,
}
    
    force_factors=list(force_mult.keys())

    inp_force=st.selectbox("From :",force_factors)
    opt_force=st.selectbox("To :",force_factors)
    force_value=st.number_input(f"Enter The Amount Of Force In :blue-background[{inp_force}] To Convert Into :blue-background[{opt_force}] :", value=0.0, step=0.01)
    newton=force_value/force_mult[inp_force]
    result=newton*force_mult[opt_force]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{force_value} {inp_force} = :green-background[{result:.2f} {opt_force}]]***') 

def time():
    time_mult={
    "Second": 1,
    "Femtosecond": 1.0000e+15,
    "Picosecond": 1.0000e+12,
    "Nanosecond": 1.0000e+9,
    "Microsecond":1000000,
    "Millisecond":1000,
    "Minute": 0.01666667,
    "Hour": 0.00027778,
    "Day":0.00001157,
    "Week":0.00000165,
    "Fortnight": 8.2672e-7,
    "Month":3.8052e-7,
    "Year": 3.1710e-8,
    "Sidereal year": 3.1688e-8,
    "Decade": 3.1710e-9,
    "Century": 3.1710e-10,
    "Millennium": 3.1710e-11,
}
    
    time_factors=list(time_mult.keys())
    inp_time=st.selectbox("From :",time_factors)
    opt_time=st.selectbox("To :",time_factors)
    time_value=st.number_input(f"Enter Time In :blue-background[{inp_time}] To Convert Into :blue-background[{opt_time}] :", value=0.0, step=0.01)
    second=time_value/time_mult[inp_time]
    result=second*time_mult[opt_time]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{time_value} {inp_time} = :green-background[{result:.2f} {opt_time}]]***') 

def pressure():
    pressure_mult={
        
    "Pascal": 1,
    "Barye": 10,
    "Millipascal": 1000,
    "Hectopascal":0.01,
    "Kilopascal":0.001,
    "Megapascal": 0.000001,
    "Gigapascal":1.0000e-9,
    "Torr": 0.00750062,
    "Psi": 0.00014504,
    "Standard atmosphere":0.00000987,
    "Technical atmosphere":0.0000102,
    "Millibar":0.01,
    "Centibar": 0.001,
    "Decibar":0.0001,
    "Bar":0.00001,
    "Kilobar": 1.0000e-8,
    "Megabar": 1.0000e-11,
    "Gigabar":1.0000e-14,
}

    pressure_factors=list(pressure_mult.keys())

    inp_pressure=st.selectbox("From :",pressure_factors)
    opt_pressure=st.selectbox("To :",pressure_factors)
    pressure_value=st.number_input(f"Enter Value Of  Pressure In :blue-background[{inp_pressure}] To Convert Into :blue-background[{opt_pressure}] :", value=0.0, step=0.01)
    pascal=pressure_value/pressure_mult[inp_pressure]
    result=pascal*pressure_mult[opt_pressure]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{pressure_value} {inp_pressure} = :green-background[{result:.2f} {opt_pressure}]]***') 



def energy():
    energy_mult={ 
        "Joule":1,
    "Kilojoule":0.001,
    "Calorie":0.23900574,
    "Kilocalorie":0.00023901,
    "Kilowatt hour":2.7778e-7,
    "British thermal unit (BTU)":0.00094782,
    "Erg": 10000000,
    "Foot pound": 0.73756215,
    "Electron volt": 6.2415e+18,
    "Decielectron volt": 6.2415e+19,
    "Centielectron volt": 6.2415e+20,
    "Millielectron volt": 6.2415e+21,
    "Microelectron volt": 6.2415e+24,
    "Nanoelectron volt": 6.2415e+27,
    "Picoelectron volt": 6.2415e+30,
    "Femtoelectron volt": 6.2415e+33,
    "Attoelectron volt":6.2415e+36,
    "Zeptoelectron volt": 6.2415e+39,
    "Yoctoelectron volt": 6.2415e+42,
    "Decaelectron volt": 6.2415e+17,
    "Hectoelectron volt": 6.2415e+16,
    "Kiloelectron volt": 6.2415e+15,
    "Megaelectron volt": 6.2415e+12,
    "Gigaelectron volt": 6.2415e+9,
    "Teraelectron volt": 6.2415e+6,
    "Petaelectron volt": 6241.50932,
    "Exaelectron volt": 6.24150932,
    "Zettaelectron volt": 0.00624151,
    "Yottaelectron volt": 0.00000624,
}


    energy_factors=list(energy_mult.keys())

    inp_energy=st.selectbox("From :",energy_factors)
    opt_energy=st.selectbox("To :",energy_factors)
    energy_value=st.number_input(f"Enter Value Of  Energy In :blue-background[{inp_energy}] To Convert Into :blue-background[{opt_energy}] :", value=0.0, step=0.01)
    joule=energy_value/energy_mult[inp_energy]
    result=joule*energy_mult[opt_energy]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{energy_value} {inp_energy} = :green-background[{result:.2f} {opt_energy}]]***') 



def  volume():
    volume_mult={
    "Liter": 1,
    "US bushel": 0.02837759,
    "US peck": 0.11351037,
    "US dry gallon":0.22702075,
    "US gallon":0.26417205,
    "US dry quart":0.90808298,
    "US quart":1.05668821,
    "US dry pint":1.81616597,
    "US pint":2.11337642,
    "US cup":4.22675284,
    "US ounce":33.8140227,
    "US tablespoon":67.6280455,
    "US teaspoon":202.884136,
    "US gill":8.45350569,
    "US beer barrel":0.00852168,
    "Oil barrel": 0.00628981,
    "Imperial bushel": 0.02749614,
    "Imperial peck": 0.10998458,
    "Imperial gallon":0.21996915,
    "Imperial quart":0.87987661,
    "Imperial pint":1.75975321,
    "Imperial ounce": 35.1950642,
    "Imperial tbsp.":56.3121028,
    "Imperial tsp.":168.936308,
    "Nanoliter":1.0000e+9,
    "Microliter":1000000,
    "Milliliter":1000,
    "Centiliter": 100,
    "Deciliter": 10,
    "Decaliter": 0.1,
    "Hectoliter": 0.01,
    "Kiloliter": 0.001,
    "Megaliter":0.000001,
    "Cubic nanometer": 1.0000e+24,
    "Cubic millimeter":1000000,
    "Cubic centimeter": 1000,
    "Cubic decimeter": 1,
    "Cubic meter": 0.001,
    "Cubic kilometer": 1.0000e-12,
    "Cubic foot": 0.03531467,
    "Cubic inch": 61.0237441,
    "Cubic yard": 0.00130795,
    "Cubic mile": 2.3991e-13,
    "Cubic rod": 0.00000786,
    "Cord": 0.0002759,
    "Hogshead": 0.00419321,
        }
    volume_factors=list(volume_mult.keys())

    inp_volume=st.selectbox("From :",volume_factors)
    opt_volume=st.selectbox("To :",volume_factors)
    volume_value=st.number_input(f"Enter Value Of  Volume In :blue-background[{inp_volume}] To Convert Into :blue-background[{opt_volume}] :", value=0.0, step=0.01)
    joule=volume_value/volume_mult[inp_volume]
    result=joule*volume_mult[opt_volume]
    st.subheader("Results:")
    st.markdown(f'***:blue-background[{volume_value} {inp_volume} = :green-background[{result:.2f} {opt_volume}]]***') 

if cat == 'Length':
    length()
elif cat == 'Temperature':
    temp()
elif cat == 'Area':
    area()
elif cat == 'Fuel Consumption':
     fuelconsumption()
elif cat == 'Digital Storage':
    digital_storage()
elif cat == 'Resistance':
    resistance()
elif cat == 'Voltage':
    voltage()
elif cat == 'Electric Current':
    electric_current()
elif cat == 'Power':
    power()
elif cat == 'Mass':
    mass()
elif cat == 'Speed':
    speed()
elif cat == 'Frequency':
    frequency()
elif cat == 'Angle':
    angle()
elif cat == 'Time':
    time()
elif cat == 'Force':
    force()
elif cat == 'Pressure':
    pressure()
elif cat == 'Energy':
    energy()
elif cat == 'Volume':
    volume()


components.html(
    "<Footer><span style=''>Developed By : Amna Rashid</span> </Footer>"
)
