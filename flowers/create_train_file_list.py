


import os
import random
import argparse

def get_list(label_name, in_dir, num):
    file_list = []
    for label, cls_name in enumerate(label_name):
        img_dir = os.path.join(in_dir, cls_name)
        print(label, cls_name, img_dir)

        imgs = os.listdir(img_dir)
        random.shuffle(imgs)
        print(len(imgs))
        # imgs = imgs[:num]
        for i in range(num):
            img_path = os.path.join(img_dir, imgs[i % len(imgs)])
            if not os.path.isfile(img_path):
                continue
            elif ' ' in img_path:
                new_file_name = img_path.replace(' ', '-')
                os.rename(img_path, new_file_name)
                img_path = new_file_name
                print('[rename] ', img_path)
            file_list.append((label, img_path))
        print(len(file_list))
    return file_list
            


def write_list(file_list, txt_file):
    with open(txt_file, 'w') as fo:
        for a in file_list:
            # fo.write('%d\t%s\n' % (a[0], a[1]))
            line = '%s %d\n' % (a[1], a[0])
            fo.write(line)


# def get_label(label_file):
#     label_name = []
#     with open(label_file, 'r'):
#         pass

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_dir', default='/media/zhangxin/DATA/data_public/slim/flower_photos_train')
    parser.add_argument('--val_dir', default='/media/zhangxin/DATA/data_public/slim/flower_photos_val')
    parser.add_argument('--train_num', default=500, type=int)
    parser.add_argument('--val_num', default=50, type=int)
    parser.add_argument('--out_dir', default='./')
    # parser.add_argument('--label_file', default='weather_label.txt')
    return parser.parse_args()

def main(args):
    label_name = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
    train_file_list = get_list(label_name, args.train_dir, args.train_num)
    val_file_list = get_list(label_name, args.val_dir, args.val_num)
    print(len(train_file_list))
    print(len(val_file_list))

    write_list(train_file_list, os.path.join(args.out_dir, 'train_file_list.txt'))
    write_list(val_file_list, os.path.join(args.out_dir, 'val_file_list.txt'))
    


if __name__ == '__main__':
    main(get_args())