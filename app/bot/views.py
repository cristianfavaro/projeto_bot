from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bot.application.update import Update
from bot.telegram import dispatcher

@csrf_exempt
def event(request):
    if not request.body:
        return HttpResponse(json.dumps({"status": "ok"}), content_type="application/json")
    
    json_request = json.loads(request.body)
    # try: 
    update = Update.de_json(json_request, dispatcher.bot)       
    dispatcher.process_update(update)

    return HttpResponse(json.dumps({"status": "ok", "content": dispatcher.bot.data}), content_type="application/json")
    # except: 
    #     return JsonResponse({"status": "error"})


