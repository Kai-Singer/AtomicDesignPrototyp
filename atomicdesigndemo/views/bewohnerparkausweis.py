from django.shortcuts import render, redirect
from django.contrib import messages
from ..utils import initApplication, addInformations, saveFile, deleteApplication, checkAge, NAVBAR_ITEMS, PLZ_PATTERN, KFZ_PATTERN
import re

### Antrag Bewohnerparkausweis Seite ###
def bewohnerparkausweis(request):

  # Beim Abschicken eines HTML-Formulars
  if request.method == "POST":

    # Erstellen des Antrags, falls noch nicht vorhanden
    form_id = request.POST.get("form_id", None)
    application_id = request.POST.get("application_id", None)
    application_id = initApplication(application_id, "bpa")

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
      if age < 18:

        # Fehlermeldung wegen zu jungem Alter
        messages.error(request, "Das Mindestalter für die Antragsstellung ist 18 Jahre!")

        # Erneutes Laden der aktuellen Seite
        return render(request, "pages/bewohnerparkausweis/01.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
      
      # Über der Altersgrenze
      else:

        # Hinzufügen der neuen Inhalte zum Antrag
        addInformations(application_id, newData)

        # Fortsetzung des Antrags
        return render(request, "pages/bewohnerparkausweis/02.html", {
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
      return render(request, "pages/bewohnerparkausweis/03.html", {
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
        return render(request, "pages/bewohnerparkausweis/03.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
      
      # Richtige PLZ
      else:

        # Hinzufügen der neuen Inhalte zum Antrag
        addInformations(application_id, newData)

        # Fortsetzung des Antrags
        return render(request, "pages/bewohnerparkausweis/04.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
    
    ### Formular Seite 4 ###
    elif form_id == "04":

      # Auslesen der übergebenen Parameter
      newData = {
        "kennzeichen": request.POST.get("bpa_kennzeichen", None),
        "kfz_typ": request.POST.get("bpa_typ", None),
        "anderer_halter": request.POST.get("bpa_halter", None),
      }

      # Falsches Kennzeichen
      if not re.match(KFZ_PATTERN, newData["kennzeichen"]):

        # Fehlermeldung wegen falschem Kennzeichen
        messages.error(request, "Das Kennzeichen ist nicht gültig! Format 'S-XX 1234' beachten!")

        # Erneutes Laden der aktuellen Seite
        return render(request, "pages/bewohnerparkausweis/04.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
      
      # Richtiges Kennzeichen
      else:

        # Hinzufügen der neuen Inhalte zum Antrag
        addInformations(application_id, newData)

        # Bei abweichendem Halter
        if newData["anderer_halter"] == "True":

          # Fortsetzung des Antrags für abweichende Halter (Abzweigung)
          return render(request, "pages/bewohnerparkausweis/05.html", {
            "navbar_items": NAVBAR_ITEMS,
            "application_id": application_id,
          })
        
        # Bei gleichem Halter
        else:

          # Fortsetzung des Antrags für gleiche Halter (Hauptzweig)
          return render(request, "pages/bewohnerparkausweis/08.html", {
            "navbar_items": NAVBAR_ITEMS,
            "application_id": application_id,
          })
    
    ### Formular Seite 5 ###
    elif form_id == "05":

      # Auslesen der übergebenen Parameter
      newData = {
        "halter_firma": request.POST.get("bpa_halter_firma", None),
        "halter_vorname": request.POST.get("bpa_halter_vorname", None),
        "halter_nachname": request.POST.get("bpa_halter_nachname", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/bewohnerparkausweis/06.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    

    ### Formular Seite 6 ###
    elif form_id == "06":
      newData = {
        "halter_strasse": request.POST.get("street", None),
        "halter_hausnummer": request.POST.get("number", None),
        "halter_plz": request.POST.get("zip_code", None),
        "halter_ort": request.POST.get("city", None),
        "halter_land": request.POST.get("country", None),
      }

      # Falsche PLZ
      if not re.match(PLZ_PATTERN, newData["halter_plz"]):

        # Fehlermeldung wegen falscher PLZ
        messages.error(request, "Die PLZ ist nicht gültig! Format '12345' beachten!")


        # Erneutes Laden der aktuellen Seite
        return render(request, "pages/bewohnerparkausweis/06.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
      
      # Richtige PLZ
      else:

        # Hinzufügen der neuen Inhalte zum Antrag
        addInformations(application_id, newData)

        # Fortsetzung des Antrags
        return render(request, "pages/bewohnerparkausweis/07.html", {
          "navbar_items": NAVBAR_ITEMS,
          "application_id": application_id,
        })
    
    ### Formular Seite 7 ###
    elif form_id == "07":

      # Auslesen der hochgeladenen Datei
      upload = request.FILES.get("upload", None)

       # Abspeichern der hochgeladenen Datei
      saveFile(application_id, "ueberlassungserklaerung", upload)

      # Auslesen der übergebenen Parameter
      newData = {
        "halter_ueberlassung": True,
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/bewohnerparkausweis/08.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular Seite 8 ###
    elif form_id == "08":

      # Auslesen der übergebenen Parameter
      newData = {
        "kein_privater_stellplatz": request.POST.get("bpa_kein_privater_stellplatz", None),
        "gueltigkeitsdauer": request.POST.get("bpa_gueltigkeitsdauer", None),
        "zahlungsart": request.POST.get("bpa_zahlungsart", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Fortsetzung des Antrags
      return render(request, "pages/bewohnerparkausweis/09.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### Formular letzten Seite 9 ###
    elif form_id == "submit":

      # Auslesen der übergebenen Parameter
      newData = {
        "bestaetigungen": request.POST.getlist("confirmation", None),
      }

      # Hinzufügen der neuen Inhalte zum Antrag
      addInformations(application_id, newData)

      # Positive Rückmeldung für den abgeschickten Antrag
      messages.success(request, "Der Antrag Bewohnerparkausweis wurde erfolgreich abgeschickt!")

      # Laden der Homepage
      return redirect('home')
    
    ### "Zurück"-Knopf des Formulars ###
    elif form_id == "back":

      # Auslesen der übergebenen ID der vorherigen Seite
      last_page = request.POST.get("last_page", None)

      # Laden der vorherigen Seite
      return render(request, f"pages/bewohnerparkausweis/{last_page}.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
    ### "Abbrechen"-Knopf des Formulars ###
    elif form_id == "abort":

      # Löschen des Antrags
      deleteApplication(application_id)

      # Negative Rückmeldung für das Abbrechen des Antrags
      messages.error(request, "Der Antrag Bewohnerparkausweis wurde abgebrochen!")

      # Laden der Homepage
      return redirect('home')
    
    ### Fallback-Funktion ###
    else:
      
      # Laden der ersten Seite des Antrags  
      return render(request, "pages/bewohnerparkausweis/01.html", {
        "navbar_items": NAVBAR_ITEMS,
        "application_id": application_id,
      })
    
  ### Beim Öffnen des Links ### 
  else:

    # Erstellen des Antrags
    application_id = initApplication(None, "bpa")

    # Laden der erste Seite des Antrags
    return render(request, "pages/bewohnerparkausweis/01.html", {
      "navbar_items": NAVBAR_ITEMS,
      "application_id": application_id,
    })