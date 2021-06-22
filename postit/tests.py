from django.test import TestCase
from postit.models import Note
from django.urls import reverse

# Create your tests here.

def createNote(alias, note):
	return Note.objects.create(alias=alias, note=note);

#Testing Models-----------------------------------

class NoteModelTest(TestCase):

	def test_NoteReturnStr(self):
		note = createNote('Ayotunde', 'This is me again')
		self.assertEqual(note.__str__(), 'Ayotunde')

#Testing VIews-------------------------------------

class NoteIndexViewTests(TestCase):
	
	def test_fetchIndexPageSuccessfully(self):
		response = self.client.get(reverse('postit:index'))
		self.assertEqual(response.status_code, 200)

	def test_fetchSingleNote(self):
		note = createNote('Short Form', 'Long form for the short form')
		response = self.client.get(reverse('postit:index'))
		self.assertQuerysetEqual(response.context['notes'],[note])

	def test_fetchMultipleNotes(self):
		note1 = createNote('Short Form', 'Long Form for the short form')
		note2 = createNote('Another short', 'This is probably longer')
		response = self.client.get(reverse('postit:index'))
		self.assertQuerysetEqual(response.context['notes'], [note2, note1])

	def test__AddNote(self):
		alias = "Testing"
		note = 'This is from the test suite'
		response = self.client.post(reverse('postit:add_note',), data = {'alias':alias, 'note':note})
		self.assertEqual(response.status_code, 302)

	def test_editNote(self):
		note = createNote('Day1', 'These are the details for day 1');
		data = {
			'alias-edit': 'Day 1 Events',
			'note-edit' :'These are for the first day',
			'note-id':note.id,
		}
		response = self.client.post(reverse('postit:update_note'), data = data)
		self.assertEqual(response.status_code, 302)

	def test_markNote(self):
		note = createNote('Day2', "This day is to be marked done")
		response = self.client.get(reverse('postit:mark_note', args = [note.id]))
		self.assertEqual(response.status_code, 302)
		#self.assertEqual(note.status, 'm')

	def test_deleteNote(self):
		note = createNote('Day3', "This testing is for the third day.")
		response = self.client.get(reverse('postit:delete_note', args = [note.id]))
		#self.assertIs(note, False)
		self.assertEqual(response.status_code, 302)