// import { useUserStore } from '@/stores/user'
import axios from 'axios'
// import router from '@/router'
// import { ElMessage } from 'element-plus'

const baseURL = 'http://127.0.0.1:8080'

const instance = axios.create({
  baseURL, // TODO 1. 基础地址，超时时间
  timeout: 100000
})

// 请求拦截器
// instance.interceptors.request.use(
//   (config) => {
//     const userStore = useUserStore()
//     if (userStore.token) {
//       config.headers.Authorization = userStore.token // TODO 2. 携带token
//     }
//     return config
//   },
//   (err) => Promise.reject(err)
// )

// 响应拦截器
// instance.interceptors.response.use(
//   (res) => {
//     if (res.data.code === 0) {
//       return res // TODO 4. 摘取核心响应数据
//     }
//     ElMessage({ message: res.data.message || '服务异常', type: 'error' })
//     return Promise.reject(res.data) // TODO 3. 处理业务失败
//   },
//   (err) => {
//     ElMessage({
//       message: err.response.data.message || '服务异常',
//       type: 'error'
//     })
//     console.log(err)
//     // if (err.response?.status === 401) {
//     //   router.push('/login') // TODO 5. 处理401错误
//     // }
//     return Promise.reject(err)
//   }
// )

export default instance
export { baseURL }
