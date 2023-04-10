from django.test import TestCase
from django.contrib.auth import get_user_model
from bot.models import UserTelegram
import json
from django.test import Client
from django.urls import reverse
from bot.dispatcher import Update
from bot.telegram import dispatcher
from unittest import mock


class TestTelegram(TestCase):
    """test the authorized user tags api"""

    def setUp(self):

        with open("bot/tests/files/simple_message.json", 'r') as j:
            json_request = json.loads(j.read())
            self.simple_message = json_request
        
        with open("bot/tests/files/simple_callback.json", 'r') as j:
            json_request = json.loads(j.read())
            self.simple_callback = json_request

        self.c = Client()

        self.user = get_user_model().objects.create_user(
            email='test@cris.com',
            username='testando',
            password='password1234',
            first_name="test",
            last_name="1",
        )

        self.usertelegram = UserTelegram.objects.create(
            first_name = "test",
            last_name = "1",
            chat_id = 867670869,
        )

    def test_user(self):
        pass

    @mock.patch('requests.post')
    def test_conversation(self, mock_post):
        from bot.models import ConversationContext

        self.simple_message['message']['text'] = '/conv'
        response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 

        #validar se ele criou a conversa
        self.assertTrue(ConversationContext.objects.filter(name="conv").exists())

        self.simple_message['message']['text'] = '/dentro_conversa'
        response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
        print(response.json())        
        
    @mock.patch('requests.post')
    def test_command(self, mock_post):

        self.simple_message['message']['text'] = '/empresas'
        response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
        print(response.json())






        # test que retornou apenas uma palavra.
        # content = json.loads(response.content)
        # self.assertEqual(content['response'][0]['method'], "sendMessage")

        # self.assertTrue(re.search("Lula", content["data"]["reply_markup"]))
        # self.assertEqual(response.status_code, 200)  
        
    # @mock.patch('requests.post')
    # def test_palavrasoptions(self, mock_post):
        
    #     self.simple_callback['callback_query']['data'] = f"palavrasoptions-{self.word.id}"

    #     response = self.c.post(reverse('event'), json.dumps(self.simple_callback), content_type='application/json') 
    #     content = json.loads(response.content)
    #     self.assertTrue("Escolha uma das opções para a palavra *Lula*" in content["data"]["text"])
    #     self.assertTrue("palavrasdeletar-1" in content["data"]["reply_markup"])

    #     # #options de palavra que nao existe 
    #     self.simple_callback['callback_query']['data'] = f"palavrasoptions-222"
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_callback), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     content = json.loads(response.content)

    # @mock.patch('requests.post')
    # def test_palavrasadicionar(self,  mock_post):

    #     #ver se petrobras está na minha lista
    #     self.assertFalse(self.usertelegram.panel.words.filter(
    #         name="bolsonaro",
    #     ).exists())

    #     # código para adicionar palavra. 
    #     self.simple_message['message']['text'] = "/palavrasadicionar"
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)

    #     content = json.loads(response.content)    
    #     self.assertEqual(content['response'][0]['method'], "sendMessage")
    #     self.assertEqual(content["data"]["text"], "Digite a palavra que você quer adicionar a sua lista e envie para mim:")

    #     #manda o nome da palavra para adicionar
    #     self.simple_message['message']['text'] = "bolsonaro"
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
    #     content = json.loads(response.content)    
        
    #     self.assertEqual(content['response'][0]['method'], "sendMessage")
    #     self.assertEqual(content['response'][1]['method'], "editMessageText")
    #     self.assertTrue("A palavra *bolsonaro* foi adicionada a sua lista com sucesso!" in content["data"]["text"])

    #     #test se a palavra foi adicionada
    #     self.assertTrue(self.usertelegram.panel.words.filter(
    #         name="bolsonaro",
    #     ).exists())

    #     self.assertFalse(getattr(self.usertelegram, 'context', False))

    #     #TENTAR ADICIONAR DE NOVO

    #     # código para adicionar palavra. 
    #     self.simple_message['message']['text'] = "/palavrasadicionar"
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
    #     self.simple_message['message']['text'] = "bolsonaro"
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
    #     content = json.loads(response.content)    
    #     self.assertTrue("Você já tem a palavra *bolsonaro* na sua lista" in content["data"]["text"])


    # @mock.patch('requests.post')
    # def test_palavrasadicionar_len_one(self,  mock_post):

    #     # código para adicionar palavra. 
    #     self.simple_message['message']['text'] = "/palavrasadicionar"
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 

    #     self.simple_message['message']['text'] = "b" 
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
    #     content = json.loads(response.content)    
    #     self.assertEqual("A palavra *b* não é válida. Precisa ter no mínimo dois caracteres...", content["data"]["text"])
        

        
    # @mock.patch('requests.post')
    # def test_delete_myword(self, mock_post):

    #     #deletar apenas a minha palavra mas nao sumir da base
    #     user_2 = get_user_model().objects.create_user(
    #         email='test2@cris.com',
    #         password='password1234',
    #         first_name="test2",
    #         last_name="12",
    #     )

    #     profile2 = Profile.objects.create(
    #         user = user_2, 
    #         email_confirmed=True
    #     )

    #     usertelegram2 = UserTelegram.objects.create(
    #         first_name = "test2",
    #         last_name = "12",
    #         chat_id = 111111,
    #     )

    #     panel2 = Panel.objects.create(profile=profile2)

    #     panel2.telegram = usertelegram2
    #     panel2.save()

    #     word3 = Word.objects.create(
    #         name = "pt",
    #     )
        
    #     word3.followers.add(panel2)
    #     word3.followers.add(self.usertelegram.panel)

    #     #testa se os dois tëm as palavras
    #     self.assertTrue(self.usertelegram.panel.words.filter(
    #         name="pt"
    #     ).exists())

    #     self.assertTrue(usertelegram2.panel.words.filter(
    #         name="pt"
    #     ).exists())

    #     #apaga agora a palavra e testa se ela sumiu. 
    #     self.simple_callback['callback_query']['data'] = f"palavrasdeletar-{word3.id}"    
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_callback), content_type='application/json') 
        
    #     #nao tá mais nele
    #     self.assertFalse(self.usertelegram.panel.words.filter(
    #         name="pt"
    #     ).exists())

    #     #palavra ainda existe 
    #     self.assertTrue(
    #         Word.objects.filter(name="pt").exists()
    #     )

    #     #apagando do outro 
    #     word3.followers.remove(self.usertelegram.panel)
    #     #palavra sumiu
    #     self.assertTrue(
    #         Word.objects.filter(name="pt").exists()
    #     )
    
    # @mock.patch('requests.post')
    # def test_palavrasdeletar(self, mock_post):
    #     self.assertTrue(self.usertelegram.panel.words.filter(
    #         name="Lula"
    #     ).exists())

    #     self.simple_callback['callback_query']['data'] = f"palavrasdeletar-{self.word.id}"    
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_callback), content_type='application/json') 
        
    #     content = json.loads(response.content)
    #     self.assertTrue("A palavra Lula foi apagada da sua lista som sucesso!" in content["data"]["text"])
    #     self.assertEqual(content['response'][0]['method'], "editMessageText")

    #     self.usertelegram.refresh_from_db()
    #     self.assertFalse(self.usertelegram.panel.words.filter(
    #         name="Lula"
    #     ).exists())

    #     #tentar apagar de novo
    #     self.simple_callback['callback_query']['data'] = f"palavrasdeletar-{self.word.id}"    
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_callback), content_type='application/json') 
        
    #     content = json.loads(response.content)
    #     self.assertTrue("Já apagada" in content["data"]["text"])

    #     # ver se apagou a palavra também como ninguém mais está usando. 
    #     lula = Word.objects.filter(name="Lula")
    #     self.assertFalse(lula)

    #     #ver se estou com a base vazia. 
    #     self.simple_message['message']['text'] = '/palavras'
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_message), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     content = json.loads(response.content)
    #     self.assertTrue("Você ainda não tem uma palavra na sua lista!" in content["data"]["text"])

    #     #tentar apagar de novo
    #     self.simple_callback['callback_query']['data'] = f"palavrasdeletar-{self.word.id}"    
    #     response = self.c.post(reverse('event'), json.dumps(self.simple_callback), content_type='application/json') 
    #     content = json.loads(response.content)
    #     self.assertTrue("Já apagada" in content["data"]["text"])
