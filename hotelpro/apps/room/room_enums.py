from enum import Enum


class STATUS(Enum):
    available = ("available", "available")
    full = ("full", "Full")
    reserved = ("reserved", "reserved")

    @classmethod
    def choices(cls):
        return [(status.value[0], status.name[1]) for status in cls]


class RoomType(Enum):
    standard_room = (
        "Standard Room",
        "A basic room with essential amenities,suitable for budget-conscious travelers.",
    )
    deluxe_room = (
        "Deluxe Room",
        "A more spacious and well-appointed room with additional amenities like a mini-fridge, coffee maker, and work desk.",
    )
    suite = (
        "Suite",
        "A larger room with separate living and sleeping areas, often equipped with a kitchenette or full kitchen.",
    )
    accessible_room = (
        "Accessible Room",
        "A room designed to accommodate guests with disabilities, featuring wider doorways, grab bars, and other accessibility features.",
    )

    pet_friendly_room = (
        "Pet-Friendly Room",
        "A room that allows guests to bring their pets, with designated pet-friendly amenities and facilities.",
    )
    connecting_rooms = (
        "Connecting Rooms",
        "Two or more rooms with a connecting door, ideal for groups or families who want to stay close together while maintaining privacy.",
    )
    executive_room = (
        "Executive Room",
        "A room designed for business travelers, typically offering extra services such as a dedicated workspace, complimentary breakfast, and access to a business lounge.",
    )

    @classmethod
    def choices(cls):
        return [(room_type.value[0], room_type.name[1]) for room_type in cls]
