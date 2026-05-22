from django import template

register = template.Library()

### Form Heading ###
@register.inclusion_tag("components/organisms/form_heading.html")
def organismFormHeading(text, application_id, last_page = None, back_disabled = False, abort_disabled = False):
  return {
    "text": text,
    "application_id": application_id,
    "last_page": last_page,
    "back_disabled": back_disabled,
    "abort_disabled": abort_disabled
  }

### Name Form ###
@register.inclusion_tag("components/organisms/name_form.html")
def organismNameForm(name, application_id, heading, description = None):
  form_of_address_options = [
    { "value": "m", "label": "Herr" },
    { "value": "w", "label": "Frau" },
    { "value": "d", "label": "Divers" },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "form_of_address_options": form_of_address_options,
  }

### Address Form ###
@register.inclusion_tag("components/organisms/address_form.html")
def organismAddressForm(name, application_id, heading, description = None):
  country_options = [
    { "value": "de", "label": "Deutschland" },
    { "value": "at", "label": "Österreich" },
    { "value": "ch", "label": "Schweiz" },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "country_options": country_options,
  }

### Contact Form ###
@register.inclusion_tag("components/organisms/contact_form.html")
def organismContactForm(name, application_id, heading, description = None):
  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
  }

###  Upload Form ###
@register.inclusion_tag("components/organisms/upload_form.html")
def organismUploadForm(name, application_id, heading, description = None):
  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
  }

### Submit Form ###
@register.inclusion_tag("components/organisms/submit_form.html")
def organismSubmitForm(name, application_id, heading, description = None):
  confirmation_options = [
    {
      "value": "privacy",
      "label": "Ich stimme der Datenverarbeitung zu",
      "required": True
    },
    {
      "value": "correctness",
      "label": "Ich habe alle Fragen wahrheitsgetreu beantwortet",
      "required": True
    },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "confirmation_options": confirmation_options,
  }

### EAK Einsatzgebiet Form ###
@register.inclusion_tag("components/organisms/eak_einsatzgebiet_form.html")
def organismEAKEinsatzgebietForm(name, application_id, heading, description = None):
  einsatzgebiet_options = [
    { "value": "feuerwehr", "label": "Freiwillige Feuerwehr" },
    { "value": "gesundheitsbereich", "label": "Gesundheitsbereich" },
    { "value": "jugendarbeit", "label": "Jugendarbeit" },
    { "value": "sozial", "label": "Sozialer Bereich" },
    { "value": "sonstige", "label": "Sonstiges (Bitte angeben)" },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "einsatzgebiet_options": einsatzgebiet_options,
  }

### EAK Ehrenamt Details Form ###
@register.inclusion_tag("components/organisms/eak_ehrenamt_details_form.html")
def organismEAKEhrenamtDetailsForm(name, application_id, heading, description = None):
  taetigkeitsort_options = [
    { "value": "freiburg", "label": "Freiburg" },
    { "value": "karlsruhe", "label": "Karlsruhe" },
    { "value": "stuttgart", "label": "Stuttgart" },
  ]

  zeiteinsatz_options = [
    { "value": "100", "label": "mind. 100 Stunden im letzten Jahr" },
    { "value": "200", "label": "mind. 200 Stunden im letzten Jahr" },
    { "value": "keine", "label": "Keine der oben genannten Bedingungen trifft zu" },
  ]

  aufwandsentschaedigung_options = [
    { "value": True, "label": "Ja" },
    { "value": False, "label": "Nein" }
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "taetigkeitsort_options": taetigkeitsort_options,
    "zeiteinsatz_options": zeiteinsatz_options,
    "aufwandsentschaedigung_options": aufwandsentschaedigung_options,
  }

###  EAK Abschluss Form ###
@register.inclusion_tag("components/organisms/eak_abschluss_form.html")
def organismEAKAbschlussForm (name, application_id, heading, description = None):
  form_options = [
    { "value": "plastik", "label": "Plastikkarte" },
    { "value": "digital", "label": "Digitale Karte" },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "form_options": form_options,
  }

###  BPA Fahrzeug Form ###
@register.inclusion_tag("components/organisms/bpa_fahrzeug_form.html")
def organismBPAFahrzeugForm(name, application_id, heading, description = None):
  typ_options = [
    { "value": "pkw", "label": "PKW" },
    { "value": "motorrad", "label": "Motorrad" },
    { "value": "sonstiges", "label": "Sonstiges" },
  ]

  halter_options = [
    { "value": False, "label": "Auf den eigenen Namen zugelassen" },
    { "value": True, "label": "Auf einen anderen Halter zugelassen" },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "typ_options": typ_options,
    "halter_options": halter_options,
  }

###  BPA Halter Form ###
@register.inclusion_tag("components/organisms/bpa_halter_form.html")
def organismBPAHalterForm(name, application_id, heading, description = None):
  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
  }

###  BPA Abschluss Form ###
@register.inclusion_tag("components/organisms/bpa_abschluss_form.html")
def organismBPAAbschlussForm (name, application_id, heading, description = None):
  kein_privater_stellplatz_options = [
    {
      "value": True,
      "label": "Ich besitze keinen privaten Stellplatz",
      "required": True
    },
  ]

  gueltigkeitsdauer_options = [
    { "value": 3, "label": "3 Monate" },
    { "value": 6, "label": "6 Monate" },
    { "value": 12, "label": "1 Jahr" },
    { "value": 24, "label": "2 Jahre" },
  ]

  zahlungsart_options = [
    { "value": "kreditkarte", "label": "Kreditkarte" },
    { "value": "lastschrift", "label": "Lastschrift" },
  ]

  return {
    "name": name,
    "application_id": application_id,
    "heading": heading,
    "description": description,
    "kein_privater_stellplatz_options": kein_privater_stellplatz_options,
    "gueltigkeitsdauer_options": gueltigkeitsdauer_options,
    "zahlungsart_options": zahlungsart_options,
  }

### Item Card List ###
@register.inclusion_tag("components/organisms/item_card_list.html")
def organismItemCardList(items = []):
  return {
    "items": items,
  }

### Navigation ###
@register.inclusion_tag("components/organisms/navigation.html")
def organismNavigation(items = []):
  return {
    "items": items,
  }

### Navigation with Search ###
@register.inclusion_tag("components/organisms/navigation_with_search.html")
def organismNavigationWithSearch(items = []):
  return {
    "items": items,
  }

### Message Container ###
@register.inclusion_tag("components/organisms/message_container.html")
def organismMessageContainer(messages = []):
  return {
    "messages": messages,
  }