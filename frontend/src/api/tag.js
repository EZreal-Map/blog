import request from '@/utils/request'

// tag：获取标签列表
export const getTagListService = () => {
  return request.get('/tag')
}
