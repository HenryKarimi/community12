{
    "name": "Cron Per Second",
    "summary": """Run cron/schedule action every second""",
    "description": """
        By default Odoo cron job or schedule action cannot be used to schedule a job in seconds interval. 
        i.e You cannot schedule a cron job to run every 5 seconds.

        This module enable running cron to the lowest time fragment. It is advisable to be use for quick and fast action that 
        will take less execution time

    """,
    "author": "Babatope Ajepe",
    "website": "http://www.galago.com.ng",
    "license": "LGPL-3",
    "price": "10.0",
    "currency": "EUR",
    "images": ["static/description/main_screenshot.png"],
    "category": "HidProductivity/Notesden",
    "version": "1.0",
    "depends": ["base"],
}
