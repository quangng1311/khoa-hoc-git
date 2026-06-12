# Du an hoc Git #

## Lệnh git đã sử dụng:
- **git init** ---           (Khởi tạo kho lưu trữ mới để bật tính năng quản lý phiên bản.)
- **git add** ---            (Gom nhóm các thay đổi có liên quan lại với nhau tại khu vực chuẩn bị, để "ghi nhận" chúng vào lịch sử.)
- **git commit** ---         (Lưu hoặc "lưu lại" các thay đổi trong khu vực dàn dựng vào lịch sử dự án.)
- **git status** ---         (Xem trạng thái hiện tại của thư mục làm việc và khu vực lưu trữ tạm thời.)
- **git checkout** ---       (Thay đổi thư mục làm việc của bạn sang một phiên bản khác từ lịch sử kho lưu trữ.)
- **git log** ---            (Hiển thị lịch sử chi tiết của dự án.)
- **git diff** ---           (Sự khác biệt giữa thư mục làm việc và khu vực dàn dựng.)
- **git revert** ---         (Đảo ngược một commit bị lỗi)
- **git branch** ---         (xem hoặc tạo nhánh)
- **git clone** ---          (tải repository từ GitHub về máy)

## Mục tiêu project:
*Các kỹ năng đã thực hành:*
- Tạo và quản lý GitHub repository
- Sử dụng các lệnh Git cơ bản
- Làm việc với branch
- Tạo pull request
- Xử lý conflict cơ bản
- Rollback/revert khi code bị lỗi
- Hiểu GitHub Flow

- ## Github flow:
*Github flow gồm các bước:*
- Bước 1: Tạo nhánh mới (Create a branch)
- Bước 2: Thêm commit (Make commits)
- Bước 3: Mở một Pull Request - PR (Open a Pull Request)
- Bước 4: Thảo luận và Đánh giá code (Discuss and Review code)
- Bước 5: Chạy thử nghiệm / Kiểm thử (Deploy for testing)
- Bước 6: Hợp nhất nhánh (Merge và Delete branch)

 BÁO CÁO HOÀN THÀNH PROJECT: THỰC HÀNH GIT & GITHUB

Repository này lưu trữ tiến độ, minh chứng hoàn thành các tiêu chuẩn đầu ra của học phần Git/GitHub, đồng thời là móng vững chắc chuẩn bị cho hành trình Vibe Coding sắp tới.

Khung Kiểm Tra Điều Kiện Hoàn Thành (Checklist)

| STT | Điều Kiện Hoàn Thành | Trạng Thái | Minh Chứng / Vị Trí Kiểm Tra |
| :---: | :--- | :---: | :--- |
| 1 | Hoàn thành các module học tập được giao | ✅ Hoàn thành | Đã học xong lý thuyết |
| 2 | Tạo GitHub repository cá nhân | ✅ Hoàn thành | Chính là Repository này |
| 3 | Có tối thiểu **10 commit** có ý nghĩa | ✅ Hoàn thành | Kiểm tra tại mục **Commits** của Repo |
| 4 | Có tối thiểu **3 branch** thực hành | ✅ Hoàn thành | Nhánh: `main`, `mimic`, `vadir` |
| 5 | Có tối thiểu **2 pull request** | ✅ Hoàn thành | Kiểm tra tại mục **Pull Requests (Closed)** |
| 6 | Có ít nhất **1 tình huống Conflict** | ✅ Hoàn thành | Đã xảy ra và xử lý trực tiếp trên file `mimic` |
| 7 | Có ít nhất **1 tình huống Rollback/Revert** | ✅ Hoàn thành | Đã thực hành lệnh `git revert HEAD` ở commit cuối |
| 8 | Nộp ảnh chụp minh chứng Microsoft Learn | ✅ Hoàn thành | (Học viên đính kèm ảnh bên dưới) |
| 9 | Mentor xác nhận đạt yêu cầu | ⏳ Chờ duyệt | Chờ đánh giá từ Mentor |

## 🔀 Tình huống giải quyết Xung đột (Conflict)

- **Mô tả tình huống:** Xung đột mã nguồn đã xảy ra tại tệp `price_tracker.py` trong quá trình gộp nhánh.
  - **Trên nhánh `main`:** Một thành viên đã cập nhật dòng chú thích cấu hình với nội dung: `thong_tin_thi_truong = "Giá SSD và RAM đang duy trì ở mức ổn định."`
  - **Trên nhánh `cap-nhat-gia`:** Cùng lúc đó, tại đúng dòng code này, dữ liệu được cập nhật sát với thực tế hơn: `thong_tin_thi_truong = "Giá SSD và DDR đang tăng giá điên cuồng do thiếu hụt nguồn cung."`
  - **Lý do báo lỗi:** Khi thực hiện thao tác Merge nhánh `cap-nhat-gia` vào `main`, hệ thống Git báo lỗi **CONFLICT (content)** vì hai luồng thông tin ghi đè lên cùng một vị trí và Git không thể tự quyết định nên giữ nhận định thị trường nào.

- **Cách giải quyết (Sử dụng GUI của Antigravity IDE):**
  1. Mở tệp `price_tracker.py` đang được báo viền màu đỏ (chứa xung đột) từ tab **Source Control**.
  2. Giao diện IDE hiển thị rõ hai đoạn code va chạm. Click chọn nút **Accept Incoming Change** (Chấp nhận thay đổi từ nhánh phụ) để giữ lại thông tin cập nhật giá chính xác nhất (giá đang tăng do thiếu hụt).
  3. Bấm `Ctrl + S` để lưu tệp.
  4. Trở lại tab Source Control, điền thông điệp: `merge: Giai quyet xung dot thong tin gia thi truong` và nhấn nút **Commit** để xác nhận hoàn tất quá trình gỡ rối.
