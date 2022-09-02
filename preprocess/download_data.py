"""Download FloorPlanCAD dataset."""
import os
import argparse
import random
import zipfile
import gdown

def unzip_sample(zip_path, unzip_dir, sample_ratio):
    """
    unzip files with a ratio
    """
    assert zipfile.is_zipfile(zip_path), f"{zip_path} is not zipfile"
    with zipfile.ZipFile(zip_path) as myzip:
        for zipinfo in myzip.infolist():
            if zipinfo.is_dir():
                continue
            # random.random()
            # 返回 [0.0, 1.0) 范围内的下一个随机浮点数。
            if random.random() >= sample_ratio:
                continue
            zipfile.ZipFile.extract(zipinfo, path=unzip_dir)


def parse_args():
    '''
    Arguments
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data_save_dir', type=str, default="./dataset",
                        help='save the downloaded data'
                        )
    parser.add_argument('--train_url', type=str,
                        default="16McNNY_-Y2uVnq42ntZTdYKPWgOZxwp3",
                        help='google drive id'
                        )
    parser.add_argument('--val_url', type=str,
                        default="1xgLqcj91i13_3vhfsUYcRYh3PhFYB9LJ",
                        help='google drive id'
                        )
    parser.add_argument('--test_url', type=str,
                        default="1Hc4-ggsUMoB_5uqJdqYRn9K73QS8rOgG",
                        help='google drive id'
                        )
    parser.add_argument('--sample_ratio', type=float,
                        default=1.0,
                        help='pick dataset'
                        )
    args = parser.parse_args()
    return args

def main():
    '''
    Main entrance
    '''
    args = parse_args()
    os.makedirs(args.data_save_dir, exist_ok=True)

    # download
    print(f'downloading train...')
    # url = f"https://drive.google.com/uc?id={args.train_url}"
    # gdown.download(url, f"{args.data_save_dir}/train.zip")
    # print(f'downloading val...')
    # url = f"https://drive.google.com/uc?id={args.val_url}"
    # gdown.download(url, f"{args.data_save_dir}/val.zip")
    # print(f'downloading test...')
    # url = f"https://drive.google.com/uc?id={args.test_url}"
    # gdown.download(url, f"{args.data_save_dir}/test.zip")

    # unzip
    zip_path = os.path.join(args.data_save_dir, "train.zip")
    unzip_dir = os.path.join(args.data_save_dir, "train")
    os.makedirs(unzip_dir, exist_ok=True)
    unzip_sample(zip_path, unzip_dir, args.sample_ratio)

    zip_path = os.path.join(args.data_save_dir, "val.zip")
    unzip_dir = os.path.join(args.data_save_dir, "val")
    os.makedirs(unzip_dir, exist_ok=True)
    unzip_sample(zip_path, unzip_dir, args.sample_ratio)

    zip_path = os.path.join(args.data_save_dir, "test.zip")
    unzip_dir = os.path.join(args.data_save_dir, "test")
    unzip_sample(zip_path, unzip_dir, args.sample_ratio)

if __name__ == '__main__':
    main()
