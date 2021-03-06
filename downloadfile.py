from enum import IntEnum

from pymongo import TEXT
from pymongo.operations import IndexModel
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
connect('mongodb://localhost:27017/youtube')
class YoutubeFileType(IntEnum):
    #unknow type ,only video data,only audio data,video and audio data
       unknow, video,audio,mix = range(4)


class YoutubeDownloadTaskType(IntEnum):
    unknow, onlyVideo, onlyAudio,merge1080P,normal = range(5)

class YoutubeDownloadStatus(IntEnum):
    unknow,error, init, start,downloading,done,discard = range(7)

class YoutubeTaskStatus(IntEnum):
    unknow,error, init, start,downloading,downloadDone,converting,converterror,convertdone,dropboxing,dropboxerror,dropboxdone = range(12)

class YoutubeDownloadTask(MongoModel):
    type = fields.IntegerField(required=True)
    vid = fields.CharField(required=True)
    status = fields.IntegerField(required=True)
    resultfilepath  = fields.CharField()
    progress = fields.IntegerField()
    videoInfo = fields.CharField()
    class Meta:
        collection_name = "youtube_downloadTask"
    # def __init__(self,type,status,vid):
    #     self.type = type
    #     self.vid = vid;
    #     self.status = status
    def __getstate__(self):
        state = self.__dict__.copy()
        data = state["_data"]
        data['_id'] = str(data['_id'])
        return data
    def __setstate__(self, state):
        self.__dict__.update(state)
class YoutubeFileDownloadData(MongoModel):
    filestorepath = fields.CharField(required=True)
    contentlength = fields.BigIntegerField(required=True)
    filetype = fields.IntegerField(required=True)
    downloadStatus = fields.IntegerField(required=True)
    url = fields.CharField(required=True)
    ext = fields.CharField(required=True)
    format = fields.CharField(required=False)
    progress = fields.IntegerField()
    task = fields.ReferenceField(YoutubeDownloadTask,required=True)



    class Meta:
        collection_name = "youtube_downloadfile"
    # def __init__(self,filestorepath,contentlength,fileype,downloadStatus,url,ext,taskid):
    #     self.filestorepath = filestorepath;
    #     self.contentlength = contentlength;
    #     self.filetype = fileype
    #     self.downloadStatus = downloadStatus
    #     self.url = url;
    #     self.ext = ext;
    #     self.taskid = taskid ;
    def __getstate__(self):
            state = self.__dict__.copy()
            data = state["_data"]
            data['_id'] = str(data['_id'])
            return data

    def __setstate__(self, state):
            self.__dict__.update(state)