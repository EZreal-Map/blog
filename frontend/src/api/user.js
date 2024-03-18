import request from '@/utils/request'

// 文章：根据ID修改文章title-content
export const putUserEmailService = (Nickname, Email) =>
  request.put(`/user`, { nickname: Nickname, email: Email })
