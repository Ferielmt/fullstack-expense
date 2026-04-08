from django.db import models
import uuid

class Transaction(models.Model):
    # Unique ID: Using UUID instead of auto-increment makes IDs harder to guess and safer for APIs. primary_key=True means this is the primary key. editable=False ensures it cannot be changed manually.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Description of the transaction (e.g., "Salary", "Groceries")
    text = models.CharField(max_length=255)
    
    # Amount of money (supports decimals, e.g., 100.50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Automatically stores the date and time when the transaction is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Special Django class for model configuration 
    class Meta:
        # Orders transactions decending by created_at field. This means when you query transactions, the most recent ones will come first. 
        ordering = ['-created_at']
    
    # Method to define string representation of the object
    def __str__(self):
        # String representation of the object (used in admin panel)
        # Example: "Salary (1500.00)"
        return f"{self.text} ({self.amount})"