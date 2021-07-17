import configparser
import cv2


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    capture = cv2.VideoCapture('http://' + config['camera']['IP'] + ':' + config['camera']['port'] + '/video')

    while True:
        _, frame = capture.read()
        cv2.imshow('stream', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()