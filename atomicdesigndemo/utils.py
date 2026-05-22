from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import date, datetime
import os, json, uuid

### Auflistung der Einträge im Navigationsmenü ###
NAVBAR_ITEMS = [
  {
    "name": "Onlineanträge",
    "url": "/home",
  },
  {
    "name": "Meine Anträge",
    "url": "",
  },
  {
    "name": "Hilfe",
    "url": "/help",
  },
]

### Auflistung der angebotenen Leistungen ###
SERVICES_LIST = [
    {
      "name": "Bewohnerparkausweis",
      "tags": [
        { "text": "Online Antrag", "color": "green" },
        { "text": "Mobilität", "color": "blue" },
        { "text": "Autofahren", "color": "purple" },
      ],
      "url": "/bewohnerparkausweis",
      "img": "bpa",
    },
    {
      "name": "Ehrenamtskarte",
      "tags": [
        { "text": "Online Antrag", "color": "green" },
        { "text": "Ehrenamt", "color": "teal" },
      ],
      "url": "/ehrenamtskarte",
      "img": "eak",
    },
  ]

### Definition der Patterns ###
PLZ_PATTERN = r"^[0-9]{5}"
KFZ_PATTERN = r"^[A-ZÄÖÜ]{1,3}-[A-Z]{1,2}\s[0-9]{1,4}[EH]?"

### Definition der Dateipfade ###
FILES_DIR = os.path.join(settings.BASE_DIR, "atomicdesigndemo", "applications")
UPLOADS_DIR = os.path.join(settings.BASE_DIR, "atomicdesigndemo", "uploads")
fs = FileSystemStorage()

### Hinzufügen eines neuen Antrags ###
def initApplication(application_id, application_type):

  # Erstellung einer neuen ID für den Antrag mit UUID
  if not application_id:
    application_id = f"{application_type}_{uuid.uuid4()}"

  # Dateipfad des Antrags
  file_path = os.path.join(FILES_DIR, f"{application_id}.json")

  # Hinzufügen des neuen Inhalts zum Antrag
  if not os.path.exists(file_path):
    with open(file_path, "w", encoding = "utf-8") as f:
      new_application = {
        "id": application_id,
        "type": application_type,
      }

      f.write(json.dumps(new_application, indent = 2, ensure_ascii = False))

  # Zurückgeben der ID des Antrags
  return application_id

### Hinzufügen von Informationen zu einem Antrag ###
def addInformations(application_id, newData):

  # Dateipfad des Antrags
  file_path = os.path.join(FILES_DIR, f"{application_id}.json")
  data = {}

  # Lesen des aktuellen Inhalts des Antrags
  with open(file_path, "r", encoding = "utf-8") as f:
    data = json.loads(f.read())

  # Überschreiben des Inhalts und Hinzufügen neuer Einträge
  for key, value in newData.items():
    data[key] = value

  # Hinzufügen des neuen Inhalts zum Antrag
  with open(file_path, "w", encoding = "utf-8") as f:
    f.write(json.dumps(data, indent = 2, ensure_ascii = False))

### Speichern einer hochgeladenen Datei ###
def saveFile(application_id, name, file):
  if file:
    extension = os.path.splitext(file.name)[1]
    file_name = f"{application_id}_upload_{name}{extension}"
    fs.save(file_name, file)

### Löschen eines Antrags ###
def deleteApplication(application_id):

  # Dateipfad des Antrags
  file_path = os.path.join(FILES_DIR, f"{application_id}.json")

  # Löschen des Antrags
  if os.path.exists(file_path):
    os.remove(file_path)

  # Löschen hochgeladener Dateien dieser ID
  for upload_file in os.listdir(UPLOADS_DIR):
    if upload_file.startswith(application_id):
      upload_file_path = os.path.join(UPLOADS_DIR, upload_file)
      os.remove(upload_file_path)

### Überprüfung des Alters ###
def checkAge(birthdate):

  # Umwandlung des Strings zu einem Datetime-Objekt
  today = date.today()
  birthday = datetime.strptime(birthdate, "%Y-%m-%d").date()

  # Alter berechnen durch eienn Tupel-Vergleich
  age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
  
  # Zurückgeben des Alters
  return age