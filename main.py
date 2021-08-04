from App.Helpers.Browser import Browser
from App.Helpers.Config import Config
from App.Models.District import District
from App.Models.Postcode import Postcode
from App.Helpers.Mail import Mail

# Postcode.postcode = "3241"
# Postcode.district = "Leiria"
# Postcode.county = "Ansião"
# Postcode.parish = "Santiago da Guarda"
# Postcode.save()

# mail = Mail()
# mail.send()

# browser = Browser()
# browser.all_counties_select()

District.where('district', 'Leiria').update([['scrapped', 1]])