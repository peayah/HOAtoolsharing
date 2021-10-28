from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique tool instances


class ToolType(models.Model):

    """Model representing a tool type."""
    name = models.CharField(max_length=200,
                            help_text='Enter a tool type (e.g. Power Tool)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Tool(models.Model):
    """Model representing a tool (but not a specific copy of a tool)."""
    tool = models.CharField(max_length=200)

    # Foreign Key used because a tool can only have one host, but hosts can have
    # multiple tools
    # Host as a string rather than object because it hasn't been declared yet in the file
    host = models.ForeignKey('Host', on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000,
                                   help_text='Enter a brief description of the tool')

    # ManyToManyField used because tool type can contain many tools.
    # ToolType class has already been defined so we can specify the object above.
    tool_type = models.ManyToManyField(ToolType, help_text='Select a type for this tool')

    def __str__(self):
        """String for representing the Model object."""
        return self.tool

    def get_absolute_url(self):
        """Returns the url to access a detail record for this tool."""
        return reverse('tool-detail', args=[str(self.id)])


class ToolInstance(models.Model):
    """Model representing a specific copy of a tool (i.e. that can be borrowed)."""
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text='Unique ID for this tool across whole collection')
    tool = models.ForeignKey('Tool', on_delete=models.RESTRICT, null=True)
    purchased = models.DateField(null=True, blank=False)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Tool availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.tool.tool})'


class Host(models.Model):
    """Model representing a host."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    house_number = models.DateField('Died', null=True, blank=True)

    STREET = (
        ('r', 'Remmington Avenue'),
        ('o', 'Ohlone Street'),
        ('a', 'Asgaard Street'),
        ('d', 'Dales Lane'),
    )

    street = models.CharField(
        max_length=1,
        choices=STREET,
        blank=True,
        default='r',
        help_text='Host street',
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular host instance."""
        return reverse('host-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

