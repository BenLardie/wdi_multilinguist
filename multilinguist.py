import requests
import json
import random

class Multilinguist:
  """This class represents a world traveller who knows
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'

    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']

class MathGenius(Multilinguist):
    """ a class about a math genius but he is also a world traveller"""

    def report_total(self, num=[]):
        num = sum(num)
        return "{} : {}".format(self.say_in_local_language('The total is'),num)


class QouteCollector(Multilinguist):
    """ a class for a lover of words and travel"""

    qoutes = [
    "Don't count the days, make the days count, Muhammad Ali",
    "'My fake plants died because I did not pretend to water them.'Mitch Hedberg'",
    "I'm retired. I was tired yesterday and I'm tired again today."
    ]

    def collector(self, qoute):
        self.qoutes.append(qoute)

    def generator(self):
        return self.say_in_local_language(random.choice(self.qoutes))


traveller_one = Multilinguist()
traveller_one.language_in('germany')
traveller_one.travel_to('Italy')
print(traveller_one.say_in_local_language("i love tacos"))
math_guy = MathGenius()
math_guy.travel_to('Italy')
print(math_guy.report_total([23,45,676,34,5778,4,23,5465]))
neil = QouteCollector()
neil.travel_to("Germany")
neil.collector("I love tacos")
print(neil.generator())
