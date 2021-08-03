from App.Helpers.Config import Config
from App.Models.Postcode import Postcode
from App.Helpers.Mail import Mail

# Postcode.postcode = "3241"
# Postcode.district = "Leiria"
# Postcode.county = "Ansião"
# Postcode.parish = "Santiago da Guarda"
# Postcode.save()

# mail = Mail()
# mail.send()

print(Config.multi_get('scrapper.locations'))