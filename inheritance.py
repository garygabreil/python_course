# # class 1
# class A:
#     #function 1
#     def featureA(self):
#         print("feature A")  
#     #function 
#     def featureB(self):
#         print("feature B")
# # class 2
# class B(A): #single inheritance
#     def featureC(self):
#         print("feature C")  
#     def featureD(self):
#         print("feature D")
#     def featureE(self):
#         print("feature E")

# class C(A): #multi-level inheritance
#     def featureG(self):
#         print("feature F")  
#     def featureG(self):
#         print("feature G")
#     def featureH(self):
#         print("feature H")

# class D(A,B,C): #multiple inheritance
#     def featureI(self):
#         print("feature I")  
#     def featureJ(self):
#         print("feature J")
#     def featureK(self):
#         print("feature K")

# b = D()
# b.featureK()



class AmazonPrime:
    def amazonVideo(self):
        print("Streaming live movies, webseries")

    def amazonRentalsVideo(self):
        print("Rental video")

class AmazonMusic:
    def amazonMusic(self):
        print("Play music")

class Amazon(AmazonMusic, AmazonPrime):  #multiple inheritance
    def amazonPay(self):
        print("Pay via amazon")


class AmazonAcquiredSpotify(AmazonMusic):
    def spotify(self):
        print("Listen music in spotify")


class AmazonAcquiredWyncMusic(AmazonMusic):
    def wync(self):
        print("Listen music in wync")

amazon = Amazon()
amazon.amazonVideo();
amazon.amazonRentalsVideo()
amazon.amazonPay();
amazon.amazonMusic();
amazon.amazonPay();

amazonAcquiredSpotify = AmazonAcquiredSpotify();
amazonAcquiredSpotify.spotify()

amazonAcquiredWyncMusic = AmazonAcquiredWyncMusic();
amazonAcquiredWyncMusic.wync()



