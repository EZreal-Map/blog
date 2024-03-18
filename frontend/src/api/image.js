import request from '@/utils/request'

// tag：获取标签列表
export const postUploadImgService = (form) => {
  return request.post('/image/upload', form, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}
