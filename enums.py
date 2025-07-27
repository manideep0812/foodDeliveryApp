from enum import Enum
class orderStatus(Enum):
    PLACED = "placed"
    PREPARED = "prepared"
    DELIVERED = "delivered"
    CANCEL = "cancel"
class paymentStatus(Enum):
    PENDING = "pending"
    INPROGRESS = "inprogress"
    COMPLETED = "completed"
    FAILED = "failed"