from dataclasses import dataclass
from Options import OptionSet, Toggle, Range, Choice, PerGameCommonOptions, TextChoice,random,ItemDict,OptionDict, DefaultOnToggle, DeathLink
from .names import item_names as iname

# class Goal(Choice):
#     """Choose your goal for the multiworld
#     - Pelly Hunt: Exctract each of the Pelly Statues from all level types
#     - Level Quota: Complete a certain number of levels in a single run"""
#     display_name: str = "Goal"
#     option_pelly_hunt = 0
#     option_level_quota = 1
#     default = 0

class PellyHunt(OptionSet):
    """Choose which Pellys will be required for victory"""
    display_name: str = "Pellys Required"
    valid_keys = {
        "Standard Pelly",
        "Glass Pelly",
        "Gold Pelly"
    }
    default = valid_keys

#class PellyCountRequired(Range):
#    """Choose how many of the 12 pellys must be found for your goal."""
#    display_name: str = "Pelly Count Required"
#    range_start = 1
#    range_end = 12
#    default = 12

class PellySpawning(DefaultOnToggle):
    """Determines how Pellys are spawned
    True: Spawns all Pellys. All Pellys are locations.
    False: Only spawns Pellys chosen in 'Pellys Required'. Only spawned Pellys are Locations."""
    display_name: str = "Pelly Spawning"

class LevelQuota(Range):
    """Choose how many levels must be completed for your goal. This is in addition to gathering all Pellys."""
    display_name: str = "Level Quota"
    range_start = 1
    range_end = 20
    default = 8

class ValuableHunt(Toggle):
    """Determines if extracting all valuables is required for your goal."""
    display_name: str = "Valuable Hunt"

class MonsterHunt(Toggle):
    """Determines if extracting all monster souls is required for your goal."""
    display_name : str = "Monster Hunt"

class CombatLogic(Choice):
    """Determines what items are logically required to fight monsters.
    Easy: Guns or Explosives
    Medium: Strength Upgrades, Melee Weapons, Guns, or Explosives
    Hard: Nothing. Player may have to use valuables found in levels."""
    display_name: str = "Combat Logic"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    default = 1

class ShopPackCount(Range):
    """Choose how many Archipelago Shop Items are unlocked with each Progressive Shop Stock."""
    display_name: str = "Progressive Shop Stock Amount"
    range_start = 5
    range_end = 50
    default = 10

class ShopUpgradeLocationsTotal(Range):
    """Choose how many Archipelago Items show up in the Upgrades section of the Shop"""
    display_name: str = "Total Shop Upgrade Locations"
    range_start = 20
    range_end = 100
    default = 80

class ShopUpgradeLocationsInLogic(Range):
    """Choose how many shop how many shop upgrades will be potentially logically relevant.
    Items past this number will not have progression items.
    This number gets set to the Total Shop Upgrade Locations if its greater.\n"""
    display_name: str = "Shop Upgrade Locations in Logic"
    range_start = 20
    range_end = 100
    default = 60

class StartingLevelType(TextChoice):
    """Choose which level type to start with"""
    display_name: str = "Starting Level Type"
    option_swiftbroom_academy = 0
    option_headman_manor = 1
    option_mcjannek_station = 2
    option_museum_of_human_art = 3
    default = "random"

class FillerItemWeights(OptionDict):
    """Choose the Weights for adding Filler to the Item Pool (death head battery and map player count do nothing in singleplayer)"""
    display_name: str = "Filler Item Weights"
    default = {
        iname.health_up : 40,
        iname.strength_up : 30,
        iname.range_up : 40,
        iname.sprint_up: 30,
        iname.stamina_up : 50, 
        #iname.player_count_up : 10,      # does nothing in singleplayer and you only need one in multiplayer
        iname.double_jump_up : 20, 
        iname.tumble_up : 20,
        iname.tumble_wings : 20,
        iname.crouch_rest : 40,
        iname.tumble_climb : 20,
        iname.death_head_battery : 10,    # does nothing in singleplayer
        iname.small_health: 20,
        iname.monster_trap: 8,
        iname.audit_trap: 6,
        iname.lure_trap: 15,
        iname.moon_phase_trap: 3    # there will never be more than 4
    }
    


@dataclass
class REPOGameOptions(PerGameCommonOptions):
    #goal: Goal
    pellys_required: PellyHunt
    #pelly_count_required: PellyCountRequired
    pelly_spawning : PellySpawning
    level_quota: LevelQuota 
    valuable_hunt: ValuableHunt
    monster_hunt: MonsterHunt
    combat_logic: CombatLogic
    shop_stock: ShopPackCount
    shop_upgrade_total: ShopUpgradeLocationsTotal
    shop_upgrade_logical: ShopUpgradeLocationsInLogic
    starting_level_type: StartingLevelType
    filler_item_weights: FillerItemWeights
    death_link: DeathLink

    
