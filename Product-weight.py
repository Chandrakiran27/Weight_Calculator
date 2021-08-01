print("Enter the following details to calcualte the prodcut weight")
"""material=["MS","SS-202","SS-304"]
length=(int(input("enter the length of the sheet")))
width=(int(input("enter the width of the sheet")))
thick=(float(input("enter the THICK of the sheet")))
area =width * length * thick
weight_MS=((area*7.850)/1000000)
weight_SS_202=((area*7.9)/1000000)
weight_SS_304=((area*8)/1000000)
print("weight of MS Sheet for",length,width, "is",weight_MS)
print("weight of SS_202 Sheet for",length,width, "is",weight_SS_202)
print("weight of SS_304 Sheet for",length,width ,"is",weight_SS_304)
"""

print("tube")
tube_available = int(input("enter 1 if tube is available in drawing"))
if tube_available == 1:
    def tube():
        a = int(input("enter the tube width"))
        b = int(input("enter the tube height"))
        c = int(input("enter the tube length"))
        d = float(input("enter the tube thickness"))

        volume = (2 * a + 2 * b) * d * c
        weight_tube_ms = (float(volume) * 7.850) / 1000000
        weight_tube_ss_202 = (float(volume) * 7.9) / 1000000
        weight_tube_ss_304 = (float(volume) * 8) / 1000000

        n = int(input("Enter the number of quantity"))
        print()
        if n > 0:
            n_ms_t = weight_tube_ms * n
            n_ss_202_t = weight_tube_ss_202 * n
            n_ss_304_t = weight_tube_ss_304 * n
            print("weight of MS tube for", a, b, c, d, "*", n, "is", n_ms_t)
            print("weight of SS_202 tube for", a, b, c, d, "*", n, "is", n_ss_202_t)
            print("weight of SS_304 tube for", a, b, c, d, "*", n, "is", n_ss_304_t)
            print()
            return n_ms_t, n_ss_202_t, n_ss_304_t
        else:
            print("quantity should not be zero")


    sum_tube_weight = []
    sum_tube_weight_ss_202 = []
    sum_tube_weight_ss_304 = []

    t = int(input(print("no of varieties")))
    for x in range(0, t):
        ms_t, ss_202_t, ss_304_t = tube()
        sum_tube_weight.append(ms_t)
        sum_tube_weight_ss_202.append(ss_202_t)
        sum_tube_weight_ss_304.append(ss_304_t)
    total_tube_weight_ms = sum(sum_tube_weight)
    total_tube_weight_ss_202 = sum(sum_tube_weight_ss_202)
    total_tube_weight_ss_304 = sum(sum_tube_weight_ss_304)
    print()
    print("total weight for all the tubes are of ms are", total_tube_weight_ms)
    print("total weight for all the tubes are of SS 202 are", total_tube_weight_ss_202)
    print("total weight for all the tubes are of SS 304 are", total_tube_weight_ss_304)
    print()
else:
    total_tube_weight_ms = 0
    total_tube_weight_ss_202 = 0
    total_tube_weight_ss_304 = 0

print("============================================")
print("rod")
rod_available = int(input("enter 1 if rod available in drawing"))
if rod_available == 1:
    def rod():
        dia = float(input("enter the dia of the rod"))
        rod_length = float(input("enter the length of rod"))
        radius = dia / 2
        rod_quantity = int(input("enter the quantity"))
        rod_area = 3.142 * (radius * radius) * rod_length
        y_rod_weight_ms = ((rod_area * 7.850) / 1000000) * rod_quantity
        y_rod_weight_ss_202 = ((rod_area * 7.9) / 1000000) * rod_quantity
        y_rod_weight_ss_304 = ((rod_area * 8) / 1000000) * rod_quantity
        print()
        print("weight of rod for MS for", dia, rod_length, "is", y_rod_weight_ms)
        print("weight of rod ss_202 for", dia, rod_length, "is", y_rod_weight_ss_202)
        print("weight of rod ss_304 is ", dia, rod_length, "is", y_rod_weight_ss_304)
        return y_rod_weight_ms, y_rod_weight_ss_202, y_rod_weight_ss_304


    r = int(input("enter the rod varieties"))
    sum_rod_weight_ms = []
    sum_rod_weight_ss_202 = []
    sum_rod_weight_ss_304 = []
    for r in range(0, r):
        rod_weight_ms, rod_weight_ss_202, rod_weight_ss_304 = rod()
        sum_rod_weight_ms.append(rod_weight_ms)
        sum_rod_weight_ss_202.append(rod_weight_ss_202)
        sum_rod_weight_ss_304.append(rod_weight_ss_304)
        print()

    total_rod_weight_ms = sum(sum_rod_weight_ms)
    total_rod_weight_ss_202 = sum(sum_rod_weight_ss_202)
    total_rod_weight_ss_304 = sum(sum_rod_weight_ss_304)

    print("total weight for all the rod are of ms are", total_rod_weight_ms)
    print("total weight for all the rod are of ss 202 are", total_rod_weight_ss_202)
    print("total weight for all the rod are of ss 304 are", total_rod_weight_ss_304)
else:
    total_rod_weight_ms = 0
    total_rod_weight_ss_202 = 0
    total_rod_weight_ss_304 = 0
print("==========================================================")
print("tray")
tray_available = int(input("press 1 to ensure the tray is available in the given drawing"))
if tray_available == 1:
    def tray():

        t_length = float(input("ENTER THE LENGTH OF THE TRAY"))
        t_width = float(input("ENTER THE width OF THE TRAY"))
        tray_thick = float(input("ENTER THE THICKNESS OF THE TRAY"))
        no_of_bends_at_length = int(input("enter the no of bends at length"))
        if no_of_bends_at_length == 0:
            tray_length = t_length
        else:
            tray_length = t_length - (2 * tray_thick)
        new_length = []
        for b in range(0, no_of_bends_at_length):
            bend = int(input("enter the bend"))
            if b == 0 or b == no_of_bends_at_length - 1:
                new_bend = bend - tray_thick
                new_length.append(new_bend)
                print(new_bend)
            else:
                new_bend = bend - (2 * tray_thick)
                new_length.append(new_bend)
                print(new_bend)
        # print(tray_length+sum(new_length))
        final_length = (tray_length + sum(new_length))
        no_of_bends_at_width = int(input("enter the no of bends at width"))
        if no_of_bends_at_width == 0:
            tray_width = t_width
        else:
            tray_width = t_width - (2 * tray_thick)
        new_width = []
        for b in range(0, no_of_bends_at_width):
            w_bend = int(input("enter the bend"))

            if b == 0 or b == no_of_bends_at_width - 1:
                new_bend_w = w_bend - tray_thick
                new_width.append(new_bend_w)
                print(new_bend_w)
            else:
                new_bend_w = w_bend - (2 * tray_thick)
                new_width.append(new_bend_w)
                print(new_bend_w)
        final_width = (tray_width + sum(new_width))
        print()
        print("THE FINAL LENGTH IS :", final_length)
        print("THE FINAL WIDTH IS ", final_width)
        print()
        n_tray = (int(input("enter the quantity")))
        area_tray = final_width * final_length
        weight_tray_ms = ((area_tray * tray_thick * 7.850) / 1000000) * n_tray
        weight_tray_ss_202 = ((area_tray * tray_thick * 7.9) / 1000000) * n_tray
        weight_tray_ss_304 = ((area_tray * tray_thick * 8) / 1000000) * n_tray
        print()
        print("MS weight of", t_length, t_width, "x", tray_thick, n_tray, "is ", weight_tray_ms)
        print("SS 202 weight of", t_length, t_width, "x", tray_thick, n_tray, "is ", weight_tray_ss_202)
        print("SS 304 weight of", t_length, t_width, "x", tray_thick, n_tray, "is ", weight_tray_ss_304)
        print()
        return weight_tray_ms, weight_tray_ss_202, weight_tray_ss_304


    final_tray_weight_ms = []
    final_tray_weight_ss_202 = []
    final_tray_weight_ss_304 = []
    tray_var = int(input("enter the number of different trays"))
    for number in range(0, tray_var):
        z_weight_tray_ms, z_weight_tray_ss_202, z_weight_tray_ss_304 = tray()
        final_tray_weight_ms.append(z_weight_tray_ms)
        final_tray_weight_ss_202.append(z_weight_tray_ss_202)
        final_tray_weight_ss_304.append(z_weight_tray_ss_304)
    total_final_tray_weight_ms = sum(final_tray_weight_ms)
    total_final_tray_weight_ss_202 = sum(final_tray_weight_ss_202)
    total_final_tray_weight_ss_304 = sum(final_tray_weight_ss_304)

    print()
    print("the total weight of ms tray is", sum(final_tray_weight_ms))
    print("the total weight of ss_202 tray is", sum(final_tray_weight_ss_202))
    print("the total weight of ss_304 tray is", sum(final_tray_weight_ss_304))
    print()

else:
    total_final_tray_weight_ms = 0
    total_final_tray_weight_ss_202 = 0
    total_final_tray_weight_ss_304 = 0
print("=======================================================================")

print("ROUND PIPE")

pipe_available = int(input("enter 1 if pipe is available in drawing"))
if pipe_available == 1:
    def pipe():
        pipe_dia = float(input("enter the dia of the pipe"))
        pipe_thick = float(input("enter the thickness of the pipe"))
        pipe_length = float(input("enter the length"))
        pipe_quantity = int(input("enter the number of quantity"))
        pipe_id = pipe_dia - (2 * pipe_thick)
        print(pipe_id)
        pipe_area = ((pipe_dia ** 2) - (pipe_id ** 2)) * pipe_length * (3.142 / 4)
        t_pipe_weight_ms = ((pipe_area * 7.850) / 1000000) * pipe_quantity
        t_pipe_weight_ss_202 = ((pipe_area * 7.9) / 1000000) * pipe_quantity
        t_pipe_weight_ss_304 = ((pipe_area * 8) / 1000000) * pipe_quantity
        print()
        print("the weight for MS pipe of ", pipe_dia, pipe_thick, pipe_length, "x", pipe_quantity, "is",
              t_pipe_weight_ms)
        print("the weight for SS 202 pipe of ", pipe_dia, pipe_thick, pipe_length, "x", pipe_quantity, "is",
              t_pipe_weight_ss_202)
        print("the weight for SS 304 pipe of ", pipe_dia, pipe_thick, pipe_length, "x", pipe_quantity, "is",
              t_pipe_weight_ss_304)
        print()
        return t_pipe_weight_ms, t_pipe_weight_ss_202, t_pipe_weight_ss_304


    sum_pipe_weights_ms = []
    sum_pipe_weights_ss_202 = []
    sum_pipe_weights_ss_304 = []
    pipe_varieties = int(input("enter the pipe varieties"))
    for pipe_v in range(0, pipe_varieties):
        pipe_weight_ms, pipe_weight_ss_202, pipe_weight_ss_304 = pipe()
        sum_pipe_weights_ms.append(pipe_weight_ms)
        sum_pipe_weights_ss_202.append(pipe_weight_ss_202)
        sum_pipe_weights_ss_304.append(pipe_weight_ss_304)

    total_pipe_weight_ms = sum(sum_pipe_weights_ms)
    total_pipe_weight_ss_202 = sum(sum_pipe_weights_ss_202)
    total_pipe_weight_ss_304 = sum(sum_pipe_weights_ss_304)
    print()
    print("The total weight of the MS pipes are ", total_pipe_weight_ms)
    print("the total weight of the SS 202 pipes are", total_pipe_weight_ss_202)
    print("the total weight of the ss 304 pipes are", total_pipe_weight_ss_304)
    print()
else:
    total_pipe_weight_ms = 0
    total_pipe_weight_ss_202 = 0
    total_pipe_weight_ss_304 = 0
print("======================================================")
print("FLAT")
flat_available = int(input("ENTER 1 IF FLAT AVAILABLE IN THE DRAWING"))
if flat_available == 1:
    def flat():
        flat_width = int(input("enter the width of the flat"))
        flat_thick = int(input("enter the thickness of the flat"))
        flat_length = int(input("enter the length of the flat"))
        flat_quantity = int(input("enter the quantity of the flat"))
        a_flat_weight_ms = (flat_width * flat_thick * flat_length * flat_quantity * 7.850) / 1000000
        a_flat_weight_ss_202 = (flat_width * flat_thick * flat_length * flat_quantity * 7.9) / 1000000
        a_flat_weight_ss_304 = (flat_width * flat_thick * flat_length * flat_quantity * 8) / 1000000
        print()
        print("weight of the Flat tube of ", flat_width, flat_thick, flat_length, "x", flat_quantity, "is",
              a_flat_weight_ms)
        print("weight of the SS 202 flat of ", flat_width, flat_thick, flat_length, "x", flat_quantity, "is",
              a_flat_weight_ss_202)
        print("weight of the SS 304 flat of ", flat_width, flat_thick, flat_length, "x", flat_quantity, "is",
              a_flat_weight_ss_304)
        print()
        return a_flat_weight_ms, a_flat_weight_ss_202, a_flat_weight_ss_304


    flat_var = int(input("enter the number of flat varieties"))
    total_flat_weight_ms = []
    total_flat_weight_ss_202 = []
    total_flat_weight_ss_304 = []

    for fl_var in range(0, flat_var):
        flat_weight_ms, flat_weight_ss_202, flat_weight_ss_304 = flat()
        total_flat_weight_ms.append(flat_weight_ms)
        total_flat_weight_ss_202.append(flat_weight_ss_202)
        total_flat_weight_ss_304.append(flat_weight_ss_304)
    final_flat_weight_ms = sum(total_flat_weight_ms)
    final_flat_weight_ss_202 = sum(total_flat_weight_ss_202)
    final_flat_weight_ss_304 = sum(total_flat_weight_ss_304)

    print()
    print("Total flat weight of MS FLAT are ", final_flat_weight_ms)
    print("Total flat weight of SS 202 FLAT are ", final_flat_weight_ss_202)
    print("Total flat weight of SS 304 FLAT are ", final_flat_weight_ss_304)
    print()
else:
    final_flat_weight_ms = 0
    final_flat_weight_ss_202 = 0
    final_flat_weight_ss_304 = 0
print("======================================================")
total_product_weight_ms = total_final_tray_weight_ms + total_rod_weight_ms + total_tube_weight_ms + \
                          total_pipe_weight_ms + final_flat_weight_ms
total_product_weight_ss_202 = total_final_tray_weight_ss_202 + total_rod_weight_ss_202 + total_tube_weight_ss_202 + \
                              total_pipe_weight_ss_202 + final_flat_weight_ss_202
total_product_weight_ss_304 = total_final_tray_weight_ss_304 + total_rod_weight_ss_304 + total_tube_weight_ss_304 + \
                              total_pipe_weight_ss_304 + final_flat_weight_ss_304

print("THE TOTAL WEIGHT OF THE PRODUCT IS FOR MS  ", total_product_weight_ms)
print("**********************************************************************")
print("THE TOTAL WEIGHT OF THE PRODUCT IS FOR SS_202  ", total_product_weight_ss_202)
print("**********************************************************************")
print("THE TOTAL WEIGHT OF THE PRODUCT IS FOR SS 304  ", total_product_weight_ss_304)
print()
print("THANK YOU")
