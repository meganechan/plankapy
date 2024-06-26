from plankapy import *


planka = Planka(API_URL, API_USER, API_PASS)

card = Card(planka)
card.build(name="Test Card", description="This is a test card", position=OFFSET)
createCard = card.create(project_name="test", board_name="test", list_name="test")

cardId = createCard['item']['id']

attachment = Attachment(planka)

attachment.build(cardId=cardId)
attachment.createAttachment(files=[('file',('รูปประกอบ.jpg',open('./tests/image.jpg','rb'),'image/jpg'))])

