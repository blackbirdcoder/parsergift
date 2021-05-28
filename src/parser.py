import utils
import data


def main():
    print(data.INTRO)
    pre_information = utils.picking_pre_information()
    goods = utils.take_goods(pre_information)
    utils.build_spreadsheet(goods)


if __name__ in '__main__':
    main()
