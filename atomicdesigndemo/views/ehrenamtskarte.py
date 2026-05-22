from django.shortcuts import render, redirect
from django.contrib import messages
from ..utils import initApplication, addInformations, saveFile, deleteApplication, checkAge, NAVBAR_ITEMS, PLZ_PATTERN
import re

### Antrag Ehrenamtskarte Seite ###
def ehrenamtskarte(request):

  # Beim Abschicken eines HTML-Formulars
  if request.method == "POST":

    # Erstellen des Antrags, falls noch nicht vorhanden
    form_id = request.POST.get("form_id", None)
    application_id = request.POST.get("application_id", None)
    application_id = initApplication(application_id, "eak")

    ### Formular Seite 1 ###
    if form_id == "01":

      # Auslesen der übergebenen Parameter
      newData = {
        "anrede": request.POST.get("form_of_address", None),
        "titel": request.POST.get("title", None),
        "vorname": request.POST.get("first_name", None),
        "nachname": request.POST.get("last_name", None),
        "geburtsdatum": request.POST.get("birth_date", None),
      }

      # Überprüfung des Alters
      age = checkAge(newData["geburtsdatum"])

      # Unter der ALtersgrenze
      if age < 14:

        # Fehlermeldung wegen zu jungem Alter
        messages.error(request, "Das Mindestalter für die Antragsstellung ist 14 Jahre!")
        
        # Erneutes Laden der aktuellen Seite
        return render(request, "pages/ehrenamtskarte/01.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })

      # Über der Altersgrenze
      else:

        # Hinzufügen der neuen Inhalte zum Antrag
        addInformations(application_id, newData)

        # Fortsetzung des Antrags
        return render(request, "pages/ehrenamtskarte/02.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
    
    ### Formular Seite 2 ###
    elif form_id == "02":

      # Auslesen der übergebenen Parameter
      newData = {
        "email": request.POST.get("email", None),
        "telefon": request.POST.get("phone", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/ehrenamtskarte/03.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular Seite 3 ###
    elif form_id == "03":

      # Auslesen der übergebenen Parameter
      newData = {
        "strasse": request.POST.get("street", None),
        "hausnummer": request.POST.get("number", None),
        "plz": request.POST.get("zip_code", None),
        "ort": request.POST.get("city", None),
        "land": request.POST.get("country", None),
      }

      # Falsche PLZ
      if not re.match(PLZ_PATTERN, newData["plz"]):

        # Fehlermeldung wegen falscher PLZ
        messages.error(request, "Die PLZ ist nicht gültig! Format '12345' beachten!")

        # Erneutes Laden der aktuellen Seite
        return render(request, "pages/ehrenamtskarte/03.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })

      # Richtige PLZ
      else:

        # Hinzufügen der neuen Inhalte zum Antrag
        addInformations(application_id, newData)

        # Fortsetzung des Antrags
        return render(request, "pages/ehrenamtskarte/04.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
    
    ### Formular Seite 4 ###
    elif form_id == "04":

      # Auslesen der übergebenen Parameter
      newData = {
        "einsatzgebiet": request.POST.getlist("eak_einsatzgebiet", None),
        "einsatzgebiet_infos": request.POST.get("eak_informationen", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/ehrenamtskarte/05.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular Seite 5 ###
    elif form_id == "05":

      # Auslesen der übergebenen Parameter
      newData = {
        "taetigkeitsort": request.POST.get("eak_taetigkeitsort", None),
        "zeiteinsatz_jahr": request.POST.get("eak_zeiteinsatz", None),
        "aufwandsentschaedigung": request.POST.get("eak_aufwandsentschaedigung", None),
        "bestaetigende_organisationen": request.POST.get("eak_organisationen", None),
        "kurzbeschreibung": request.POST.get("eak_kurzbeschreibung", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/ehrenamtskarte/06.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular Seite 6 ###
    elif form_id == "06":

      # Auslesen der hochgeladenen Datei
      upload = request.FILES.get("upload", None)

      # Abspeichern der hochgeladenen Datei
      saveFile(application_id, "bestaetigung", upload)

      # Auslesen der übergebenen Parameter
      newData = {
        "bestaetigung": True,
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/ehrenamtskarte/07.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular Seite 7 ###
    elif form_id == "07":

      # Auslesen der übergebenen Parameter
      newData = {
        "kartenform": request.POST.getlist("eak_form", None),
        "mitteilungen": request.POST.get("eak_mitteilung", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/ehrenamtskarte/08.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular letzten Seite 8 ###
    elif form_id == "submit":

      # Auslesen der übergebenen Parameter
      newData = {
        "bestaetigungen": request.POST.getlist("confirmation", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Positive Rückmeldung für den abgeschickten Antrag
      messages.success(request, "Der Antrag Ehrenamtskarte wurde erfolgreich abgeschickt!")

      # Laden der Homepage
      return redirect('home')
    
    ### "Zurück"-Knopf des Formulars ###
    elif form_id == "back":

      # Auslesen der übergebenen ID der vorherigen Seite
      last_page = request.POST.get("last_page", None)

      # Laden der vorherigen Seite
      return render(request, f"pages/ehrenamtskarte/{last_page}.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### "Abbrechen"-Knopf des Formulars ###
    elif form_id == "abort":

      # Löschen des Antrags
      deleteApplication(application_id)

      # Negative Rückmeldung für das Abbrechen des Antrags
      messages.error(request, "Der Antrag Ehrenamtskarte wurde abgebrochen!")

      # Laden der Homepage
      return redirect('home')
    
    ### Fallback-Funktion ###
    else:
      
      # Laden der ersten Seite des Antrags
      return render(request, "pages/ehrenamtskarte/01.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })

  ### Beim Öffnen des Links ### 
  else:

    # Erstellen des Antrags
    application_id = initApplication(None, "eak")

    # Laden der erste Seite des Antrags
    return render(request, "pages/ehrenamtskarte/01.html", {
      "navbar_items": NAVBAR_ITEMS,
      "application_id": application_id,
    })