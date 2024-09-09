
from telegram import Update

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .dispatcher import dispatcher, bot
@csrf_exempt
def message_handler(request):
    update = Update.de_json(json.loads(request.body), bot)
    dispatcher.process_update(update)
    return JsonResponse({"ok": True})

