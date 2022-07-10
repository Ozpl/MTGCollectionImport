from cmath import e
import os
import json

with open(r"C:\Users\Ozpl\Downloads\Current Collection.csv", "w") as fileW:
    fileW.close()

with open(r"C:\Users\Ozpl\Downloads\myCollection.csv", "r") as fileR:
    sets = dict()
    setsUnique = 0
    format = 2  # 1 - Decked, 2 - Moxfield

    # Decked format
    if format == 1:
        with open(r"C:\Users\Ozpl\Downloads\Current Collection.csv", "a") as fileW:
            fileW.write("Set,Card,Regular,Foil\n")
    # Moxfield format
    if format == 2:
        with open(r"C:\Users\Ozpl\Downloads\Current Collection.csv", "a") as fileW:
            fileW.write(
                r'Count,"Tradelist Count",Name,Edition,"Card Number",Condition,Foil,Signed,"Artist Proof","Altered Art",Misprint,Promo,Textless,"My Price"'
            )

    fileRlines = fileR.readlines()

    for line in fileRlines:
        # Skip first line: "Edition,"Name",0,Count"
        if line == fileRlines[0]:
            continue
        string = line

        # Format oryginaĹ‚u - Deckbox do Decked Builder
        # https://mtgcollectionbuilder.com/export
        # https://deckedstudios.supportbee.io/1893-faq/3896-decked-builder/13341-dec-and-coll-file-format
        # https://csv.deckedbuilder.com

        counter = 0
        length = len(string)
        arrPlace = []
        apostr = False

        for letter in string:
            if letter == '"':
                if apostr == False:
                    apostr = True
                else:
                    apostr = False
            if letter == "," and apostr is not True:
                arrPlace.append(counter)
            counter = counter + 1

        count = string[0 : arrPlace[0]]
        tradelistCount = string[arrPlace[0] + 1 : arrPlace[1]]
        name = string[arrPlace[1] + 1 : arrPlace[2]]
        name = name.replace('"', "")
        edition = string[arrPlace[2] + 1 : arrPlace[3]]
        edition = edition.replace('"', "")
        cardNumber = string[arrPlace[3] + 1 : arrPlace[4]]
        condition = string[arrPlace[4] + 1 : arrPlace[5]]
        foil = string[arrPlace[5] + 1 : arrPlace[6]]
        signed = string[arrPlace[6] + 1 : arrPlace[7]]
        artistProof = string[arrPlace[7] + 1 : arrPlace[8]]
        alteredArt = string[arrPlace[8] + 1 : arrPlace[9]]
        misprint = string[arrPlace[9] + 1 : arrPlace[10]]
        promo = string[arrPlace[10] + 1 : arrPlace[11]]
        textless = string[arrPlace[11] + 1 : arrPlace[12]]
        myPrice = string[arrPlace[12] + 1 : len(string)]

        # Exceptions
        x = range(1, 500)
        for n in x:
            if " (" + str(n) + ")" in name:
                name = name.replace(" (" + str(n) + ")", "")
        for n in x:
            if " (" + str(n) + " Full Art)" in name:
                name = name.replace(" (" + str(n) + " Full Art)", "")

        # if "Commander Anthology Volume II" in edition: edition = "Commander 2016"
        if "Battle for Baldur's Gate" in edition:
            edition = "Commander Legends: Battle for Baldur's Gate"
        if "Commander Anthology Volume II" in edition:
            edition = "Commander Anthology 2018"
        if "Commander 2013" in edition:
            edition = "Commander 2013 Edition"
        if "Forgotten Realms Variants" in edition:
            edition = "Adventures in the Forgotten Realms"
        if "Ikoria Variants" in edition:
            edition = "Ikoria: Lair of Behemoths"
        if "Mystery Booster Playtest Cards 2021" in edition:
            edition = "Mystery Booster Playtest Cards"
        if "Mystical Archive" in edition:
            edition = "Strixhaven Mystical Archive"
        if "Promo Pack: Forgotten Realms" in edition:
            edition = "Adventures in the Forgotten Realms"
        if "Promo Pack: Ikoria" in edition:
            edition = "Ikoria: Lair of Behemoths"
        if "Promo Pack: Innistrad Midnight Hunt" in edition:
            edition = "Innistrad: Midnight Hunt"
        if "Promo Pack: Theros Beyond Death" in edition:
            edition = "Theros Beyond Death"
        if "Promo Pack: Throne of Eldraine" in edition:
            edition = "Throne of Eldraine"
        if "Promo Pack: Zendikar Rising" in edition:
            edition = "Zendikar Rising"
        if "Ravnica Allegiance Guild Kits" in edition:
            edition = "RNA Guild Kit"
        if "Store Championship Promos" in edition:
            edition = "Wizards Play Network 2021"
        if "Strixhaven" in edition and not "Mystical Archive" in edition:
            edition = "Strixhaven: School of Mages"
        if "Time Spiral Remastered (Timeshifted)" in edition:
            edition = "Time Spiral Remastered"

        if " Variants" in edition:
            edition = edition.replace(" Variants", "")
        if " Showcase" in name:
            name = name.replace(" Showcase", "")
        if " (Borderless)" in name:
            name = name.replace(" (Borderless)", "")
        if " (Foil Etched)" in name:
            name = name.replace(" (Foil Etched)", "")
        if " (Showcase)" in name:
            name = name.replace(" (Showcase)", "")
        if " (Extended Art)" in name:
            name = name.replace(" (Extended Art)", "")
        if " (Retro Frame)" in name:
            name = name.replace(" (Retro Frame)", "")
        if " (a)" in name:
            name = name.replace(" (a)", "")
        if " (b)" in name:
            name = name.replace(" (b)", "")
        if " (No PW Symbol)" in name:
            name = name.replace(" (No PW Symbol)", "")
        if " (Dracula)" in name:
            name = name.replace(" (Dracula)", "")
        if " (Skyscraper)" in name:
            name = name.replace(" (Skyscraper)", "")
        if " (Gilded Foil)" in name:
            name = name.replace(" (Gilded Foil)", "")
        if " (Thick Stock)" in name:
            name = name.replace(" (Thick Stock)", "")

        # Guilds of Ravnica Guild Kits
        if "Guilds of Ravnica Guild Kits" in edition:
            if "Izoni, Thousand-Eyed" in name:
                edition = "Guilds of Ravnica"
            if "Forest" in name:
                edition = "Guilds of Ravnica"
            if "Swamp" in name:
                edition = "Guilds of Ravnica"
            if "Darkblast" in name:
                edition = "Ravnica: City of Guilds"
            if "Elves of Deep Shadow" in name:
                edition = "Ravnica: City of Guilds"
            if "Golgari Rot Farm" in name:
                edition = "Ravnica: City of Guilds"
            if "Golgari Signet" in name:
                edition = "Ravnica: City of Guilds"
            if "Grave-Shell Scarab" in name:
                edition = "Ravnica: City of Guilds"
            if "Putrefy" in name:
                edition = "Ravnica: City of Guilds"
            if "Savra, Queen of the Golgari" in name:
                edition = "Ravnica: City of Guilds"
            if "Shambling Shell" in name:
                edition = "Ravnica: City of Guilds"
            if "Sisters of Stone Death" in name:
                edition = "Ravnica: City of Guilds"
            if "Stinkweed Imp" in name:
                edition = "Ravnica: City of Guilds"
            if "Vigor Mortis" in name:
                edition = "Ravnica: City of Guilds"
            if "Abrupt Decay" in name:
                edition = "Return to Ravnica"
            if "Deadbridge Goliath" in name:
                edition = "Return to Ravnica"
            if "Deathrite Shaman" in name:
                edition = "Return to Ravnica"
            if "Golgari Charm" in name:
                edition = "Return to Ravnica"
            if "Grisly Salvage" in name:
                edition = "Return to Ravnica"
            if "Jarad, Golgari Lich Lord" in name:
                edition = "Return to Ravnica"
            if "Korozda Guildmage" in name:
                edition = "Return to Ravnica"
            if "Lotleth Troll" in name:
                edition = "Return to Ravnica"
            if "Slum Reaper" in name:
                edition = "Return to Ravnica"
            if "Treasured Find" in name:
                edition = "Return to Ravnica"
            if "Golgari Guildgate" in name:
                edition = "Return to Ravnica"
            if "Deadbridge Chant" in name:
                edition = "Dragon's Maze"
            if "Drown in Filth" in name:
                edition = "Dragon's Maze"
            if "Gaze of Granite" in name:
                edition = "Dragon's Maze"

        # Individual cards
        if "Athreos, Shroud-Veiled" in name and "Buy-a-Box Promos" in edition:
            edition = "Theros Beyond Death"
        if "Atris, Oracle of Half-Truths" in name and "Prerelease Cards" in edition:
            edition = "Theros Beyond Death"
        # if "Budoka Gardener // Dokai, Weaver of Life" in name and "Commander 2018" in edition: edition = "Commander Anthology 2018"
        if "Bolas's Citadel" in name and "Love Your LGS" in edition:
            edition = "Love Your LGS 2021"
        if "Chord of Calling" in name and "Prerelease Cards" in edition:
            edition = "Double Masters"
        if "Courser of Kruphix" in name and "Clash Pack Promos" in edition:
            edition = "Born of the Gods"
        if "Earthquake" in name and "Commander 2016" in edition:
            edition = "Commander Anthology 2018"
        if "Emergent Ultimatum" in name and "Prerelease Cards" in edition:
            edition = "Ikoria: Lair of Behemoths"
        if "Gilded Lotus" in name and "Promo Pack: Core Set 2020" in edition:
            edition = "Dominaria"
        if "Goblin Token" in name and "Duel Decks: Speed vs. Cunning" in edition:
            name = "Goblin"
        if "Golden Guardian // Gold-Forge Garrison" in name:
            name = "Golden Guardian"
        if "Henzie Toolbox Torre" in name:
            name = 'Henzie ""Toolbox"" Torre'
        if "Herald's Horn" in name and "The List" in edition:
            edition = "Commander 2017"
        if "Hero's Downfall" in name and "Clash Pack Promos" in edition:
            edition = "Theros"
        if "Inferno Titan" in name and "Commander 2016" in edition:
            edition = "Commander Anthology 2018"
        if "Jaxis, the Troublemaker" in name and "Buy-a-Box Promos" in edition:
            edition = "Streets of New Capenna"
        if (
            "Kenrith, the Returned King (Non-Foil)" in name
            and "Buy-a-Box Promos" in edition
        ):
            edition = "Throne of Eldraine"
            name = "Kenrith, the Returned King"
        if "Lizard Blades" in name and "Promo Pack: Kamigawa" in edition:
            edition = "Kamigawa: Neon Dynasty"
        if "Marit Lage Token" in name:
            continue
        if "Necropolis Fiend" in name and "Clash Pack Promos" in edition:
            edition = "Khans of Tarkir"
        if "Realmwalker" in name and "Buy-a-Box Promos" in edition:
            edition = "Kaldheim"
        if "Reaper of the Wilds" in name and "Clash Pack Promos" in edition:
            edition = "Theros"
        if "Satoru Umezawa" in name and "Prerelease Cards" in edition:
            edition = "Kamigawa: Neon Dynasty"
        if "Sengir, the Dark Baron" in name and "Prerelease Cards" in edition:
            edition = "Commander Legends"
        if "Sultai Ascendancy" in name and "Clash Pack Promos" in edition:
            edition = "Khans of Tarkir"
        if "Tatsunari, Toad Rider" in name and "Prerelease Cards" in edition:
            edition = "Kamigawa: Neon Dynasty"
        if "Voldaren Estate" in name and "Buy-a-Box Promos" in edition:
            edition = "Innistrad: Crimson Vow"
        if "Vorosh, the Hunter" in name and "Commander 2016" in edition:
            edition = "Commander Anthology 2018"
        if "Whip of Erebos" in name and "Clash Pack Promos" in edition:
            edition = "Theros"
        if "Yusri, Fortune's Flame" in name and "Bundle Promos" in edition:
            edition = "Modern Horizons 2"

        setsUnique = setsUnique + 1
        sets[edition] = sets.get(edition, 0) + 1 * int(count)

        # Decked format
        if format == 1:
            with open(r"C:\Users\Ozpl\Downloads\Current Collection.csv", "a") as fileW:
                if foil == "":
                    fileW.write(edition + ',"' + name + '",' + count + ",0\n")
                else:
                    fileW.write(edition + ',"' + name + '",0,' + count + "\n")
        # Moxfield format
        if format == 2:
            with open(r"C:\Users\Ozpl\Downloads\Current Collection.csv", "a") as fileW:
                name = '"' + name + '"'
                if "Talisman of Resilience" in name and "" in edition:
                    edition = "H1R"
                if "Dig Through Time" in name and "Love Your LGS" in edition:
                    edition = "Love Your LGS 2021"
                if "Reliquary Tower" in name and "Love Your LGS" in edition:
                    edition = "Love Your LGS 2020"
                # if "Arbor Elf" in name and "" in edition: edition = "PW21"
                if "Arbor Elf" in name and "Wizards Play Network 2021" in edition:
                    edition = "PW21"
                if "Arbor Elf" in name and "Store Championship Promos" in edition:
                    edition = "PW21"
                if "Commander 2016" in edition:
                    edition = "Commander Anthology Volume II"
                if (
                    "Atris, Oracle of Half-Truths" in name
                    and "Prerelease Cards" in edition
                ):
                    edition = "Theros Beyond Death Promos"
                if "Emergent Ultimatum" in name and "Prerelease Cards" in edition:
                    edition = "Ikoria: Lair of Behemoths Promos"
                if "Tatsunari, Toad Rider" in name and "Prerelease Cards" in edition:
                    edition = "Kamigawa: Neon Dynasty Promos"
                if "Satoru Umezawa" in name and "Prerelease Cards" in edition:
                    edition = "Kamigawa: Neon Dynasty Promos"
                fileW.write(
                    count
                    + ",,"
                    + name
                    + ',"'
                    + edition
                    + '",'
                    + cardNumber
                    + ",,"
                    + foil
                    + ",,,,,,,"
                    + myPrice
                )

    print("Sets alphabetically:\n")
    for key in sorted(sets):
        print("%s: %s" % (key, sets[key]))
    cardcount = 0
    for key in sets:
        cardcount = cardcount + sets[key]
    print(
        "\n\nCard count is: {0} ({1} of them are unique)\n\n".format(
            cardcount, setsUnique
        )
    )

fileR.close()
fileW.close()
