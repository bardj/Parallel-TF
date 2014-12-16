library(CENTIPEDE)
args<-commandArgs(TRUE)

inFile <- args[1]
x = read.csv(file=inFile,header=FALSE)

outFile = paste(inFile,".out")
outpng = paste(inFile,".png")

centFit <- fitCentipede(Xlist = list(Dnase=as.matrix(x)),DampNegBin=.1)
length(centFit)
length(centFit$PostPr) < 0.05

png(file=outpng)
plotProfile(centFit$LambdaParList[[1]],Mlen=21)
dev.off()

total = length(centFit$PostPr)
significant= sum(centFit$PostPr < 0.05)
ratio = (significant*100/total)
write.csv(ratio,file=outFile)

