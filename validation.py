from typing import Optional

from pydantic import BaseModel, Field


class Conference(BaseModel):
    Event_Type: Optional[str] = Field(alias="Event Type")
    Presentation: Optional[str] = Field(alias="Presentation")
    Website_URL: Optional[str] = Field(alias="Website URL")
    Location: Optional[str] = Field(alias="Location")
    Venue: Optional[str] = Field(alias="Venue")
    Date: Optional[str] = Field(alias="Date")
    Organization: Optional[str] = Field(alias="Organization")
    Conference_Tags: Optional[str] = Field(alias="Conference Tags")
    Description: Optional[str] = Field(alias="Description")
