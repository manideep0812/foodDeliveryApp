from enum import Enum
class orderStatus(Enum):
    PLACED = "placed"
    PREPARED = "prepared"
    OUTFORDELIVERY = "out-for-delivery"
    DELIVERED = "delivered"
    CANCEL = "cancel"
class paymentStatus(Enum):
    PENDING = "pending"
    INPROGRESS = "inprogress"
    COMPLETED = "completed"
    FAILED = "failed"