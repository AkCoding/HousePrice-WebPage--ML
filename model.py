from wtforms import Form, IntegerField, StringField, validators

class InputForm(Form):
    bath = IntegerField("bathrooms", validators=[validators.DataRequired()])
    balcony = IntegerField("balcony", validators=[validators.DataRequired()])
    total_sqft_int = IntegerField("total_sqft_int", validators=[validators.DataRequired()])
    bhk = IntegerField("bhk",validators=[validators.DataRequired()])
    price_per_sqft = IntegerField("price_per_sqft", validators=[validators.DataRequired()])
    availability = StringField("availability", validators=[validators.DataRequired()])
    area_type = StringField("area_type", validators=[validators.DataRequired()])
    location = StringField("location", validators=[validators.DataRequired()])

