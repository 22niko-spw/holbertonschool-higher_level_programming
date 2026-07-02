#!/usr/bin/python3
"""Module de templating simple : génère des fichiers d'invitation
personnalisés à partir d'un template et d'une liste d'attendees."""
import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """Génère un fichier output_X.txt par attendee en remplaçant
    les placeholders du template par les valeurs du dictionnaire.

    Args:
        template (str): texte contenant {name}, {event_title},
            {event_date}, {event_location}.
        attendees (list): liste de dictionnaires (un par invité).
    """
    # 1. Vérification des types d'entrée
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logging.error("Attendees must be a list of dictionaries.")
        return

    # 2. Vérification des entrées vides
    if template == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    # 3. Traitement de chaque attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, "w") as f:
            f.write(content)
