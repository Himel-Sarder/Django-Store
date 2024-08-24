from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = 'initial_name'  # Set default initial value for name field
        self.fields['email'].initial = 'initial_email'  # Set default initial value for email field

    def clean_name(self):
        value = self.cleaned_data.get('name')  # Get the cleaned data for the 'name' field
        num_of_w = value.split(' ')  # Split the name into words based on spaces
        
        if len(num_of_w) > 3:  # Check if there are more than 3 words
            self.add_error('name', 'Name can have a maximum of 3 words')  # Add an error if validation fails
        else:
            return value  # Return the value if validation passes
