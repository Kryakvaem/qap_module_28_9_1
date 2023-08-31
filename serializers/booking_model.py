from pydantic import BaseModel, Field

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class BookingResponseModel(BaseModel):
    firstname: str = Field(..., description="Firstname for the guest who made the booking")
    lastname: str = Field(..., description="Lastname for the guest who made the booking")
    totalprice: int = Field(..., description="The total price for the booking")
    depositpaid: bool = Field(..., description="Whether the deposit has been paid or not")
    bookingdates: dict = Field(..., description="Sub-object that contains the checkin and checkout dates")
    additionalneeds: str = Field(None, description="Any other needs the guest has")

    class Config:
        allow_population_by_field_name = True


class CreateBookingRequest(BaseModel):
    firstname: str = Field(..., description="Firstname for the guest who made the booking")
    lastname: str = Field(..., description="Lastname for the guest who made the booking")
    totalprice: int = Field(..., description="The total price for the booking")
    depositpaid: bool = Field(..., description="Whether the deposit has been paid or not")
    bookingdates: BookingDates = Field(..., description="Dates for check-in and check-out")
    additionalneeds: str = Field(..., description="Any other needs the guest has")

class BookingResponse(BaseModel):
    bookingid: int
    booking: CreateBookingRequest


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

class CreateBookingResponse(BaseModel):
    bookingid: int