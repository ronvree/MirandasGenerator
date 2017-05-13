import random

from PIL import Image

from I.ties.tie import Tie


def random_rgb_color():
    return random.choice(range(256)), random.choice(range(256)), random.choice(range(256))


def enhance(img, magnifier=10):
    pixels = img.load()
    enhanced_image = Image.new('RGB', (img.width * magnifier, img.height * magnifier), 'grey')
    enhanced_pixels = enhanced_image.load()
    for x in range(img.width):
        for y in range(img.height):
            for dx in range(magnifier):
                for dy in range(magnifier):
                    enhanced_pixels[x * magnifier + dx, y * magnifier + dy] = pixels[x, y]
    return enhanced_image

number_of_colors = 3
seed_bits = 2048

colors = list()
for c in range(number_of_colors):
    colors.append(random_rgb_color())

# colors = [(50, 50, 50), (150, 150, 150), (200, 200, 200)]
# colors = [(29, 58, 220), (20, 153, 184), (4, 15, 78)]

# colors = [(198, 189, 7), (238, 57, 142), (246, 127, 6)]

init_state_seed = int(random.getrandbits(seed_bits))
rule_seed = int(random.getrandbits(seed_bits))

# init_state_seed = 12864395474753824512817206686224437187699315507863591304035075195434469834093954901179249020547098791933442895459294355705793476160562674233946200999548839197855087574274078544820796265079360417546972748789400651812789226712416850472586083759244565027361925779266072440879906105970461029222989059144343610284396162228215255823979398325562798385165314435359993309018194194604329409863858748509185271142686653224164830824879828935944492058912487544012874044126425625510239436244908687047608614902805360996354378850198232482685638501247190676882842649577387814096320674472684297679531470691043703600681780045857567910412
# rule_seed = 7628987430309607096557636709197316194189937081111373985513469623135676490398811613179396087035101097937226239647946823760968003567416922367485077928455224810419585828278999918289934667967170202387603516594920742944450451220806771722288775854618668398212956491683476083220938889649505189660174989827226394369758033078545811053507393251359974385895780797847411164190471482418371885969867279680389616486920206484702277258196273639874289462339815527411597717660666273021565629110761046671091975548470118074835734465085651336803713614648569932163573249623601617122519189820956847576762246436974469550275661866713962428538

print(colors)
print(init_state_seed)
print(rule_seed)

tie = Tie(200, 50, colors, (init_state_seed, rule_seed))

image = tie.get_pattern_image()

resized = image.resize((image.width * 10, image.height * 10))

resized.save("result.png")

# image.save("result.png")

# enhanced_image = enhance(image, 10)

# enhanced_image.save("result.png")

