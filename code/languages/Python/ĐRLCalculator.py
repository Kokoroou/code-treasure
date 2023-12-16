import os

os.system("cls")

tieuChiHocTap = {
	"1": ["Có kết quả học tập ở mức: GPA >= 3.6", 18],
	"2": ["Có kết quả học tập ở mức: 3.6 > GPA >= 3.2", 16],
	"3": ["Có kết quả học tập ở mức: 3.2 > GPA >= 2.5", 14],
	"4": ["Có kết quả học tập ở mức: 2.5 > GPA >= 2.0", 12],
	"5": ["Có kết quả học tập ở mức: 2.0 > GPA >= 1.5", 10],
	"6": ["Có kết quả học tập ở mức: 1.5 > GPA", 0],
	"7": ["Đạt yêu cầu theo tiến độ của chương trình đào tạo", 4],
	"8": ["Đạt chứng chỉ ngoại ngữ tương đương TOEIC 600 điểm trở lên", 2],
	"9": ["Tham gia các hoạt động, sự kiện liên quan đến NCKH, học thuật, chuyên môn", 2],
	"10": ["Có công bố khoa học tại Hội nghị hoặc tạp chí khoa học chuyên ngành", 2],
	"11": ["Thành viên CLB học thuật/Lab/Nhóm nghiên cứu,...", 2],
	"12": ["Tham gia CLB hỗ trợ học tập", 3],
	"13": ["Tham gia các cuộc thi Olympic cấp trường, cấp quốc gia, quốc tế", 2],
	"14": ["Đạt giải trong các cuộc thi SV NCKH, Olympic, thi khoa học kỹ thuật", 2],
}
tieuChiKyLuat = {
	"1": ["Tham gia 100% buổi sinh hoạt công dân/họp lớp do Trường/Viện/Lớp tổ chức", 10],
	"2": ["Tham gia từ 50% buổi sinh hoạt công dân, họp lớp do Trường/Viện/Lớp tổ chức trở lên", 5],
	"3": ["Chấp hành quy định và quy chế của Nhà trường (không vi phạm)", 6],
	"4": ["Tham gia thực tập tăng cường năng lực nghề nghiệp tại doanh nghiệp", 2],
	"5": ["Tham gia hội thảo, khóa đào tạo tăng cường kỹ năng mềm, ý thức làm việc", 2],
	"6": ["Tham gia các buổi nói chuyện thời sự, phòng chống tội phạm và tệ nạn xã hội", 2],
	"7": ["Tham gia hoạt động hướng nghiệp, sự kiện chính trị - xã hội", 2],
}
tieuChiXaHoi = {
	"1": ["Tham gia hoạt động văn hoá (các phòng trào văn nghệ, thi SVBK,... của Viện, Trường)", 7],
	"2": ["Tham gia các giải thể thao của Viện, Trường hoặc các tổ chức hợp pháp", 8],
	"3": ["Tham gia hoạt động tình nguyện (mùa hè xanh, tình nguyện tại chỗ, cổng trường ATGT)", 3],
	"4": ["Tham gia phong trào \"cốc trà đá vì cộng đồng\",\" tuổi trẻ Bách khoa Nhân ái\"", 3],
	"5": ["Tham gia hiến máu nhân đạo do Trường và các tổ chức phát động", 6],
	"6": ["Tham gia các diễn đàn sinh viên, các buổi toạ đàm với lãnh đạo Viện, Trường", 3],
	"7": ["Có các hành động tích cực trên các trang mạng xã hội phù hợp với chủ trương của Nhà trường, Nhà nước được tập thể ghi nhận", 3],
	"8": ["Cán bộ lớp, Đoàn - Hội hoàn thành xuất sắc nhiệm vụ được tập thể công nhận", 6],
	"9": ["Cán bộ lớp, Đoàn - Hội hoàn thành tốt nhiệm vụ được tập thể công nhận", 4],
	"10": ["Cán bộ lớp, Đoàn - Hội hoàn thành nhiệm vụ được tập thể công nhận ", 2],
	"11": ["Cán bộ lớp, Đoàn - Hội không hoàn thành nhiệm vụ được tập thể công nhận", 0],
}
tieuChiCongDong = {
	"1": ["Chấp hành pháp luật của Nhà nước, quy định của nơi cư trú", 10],
	"2": ["Tham gia tuyên truyền chủ trương của Đảng, chính sách pháp luật của Nhà nước, quy định của nơi cư trú, giữ gìn an ninh – trật tự, bảo vệ sinh cảnh quan - môi trường, nếp sống văn minh nơi công cộng", 6],
	"3": ["Được khen thưởng khi tham gia tuyên truyền chủ trương của Đảng, chính sách pháp luật của Nhà nước, quy định của nơi cư trú, giữ gìn an ninh – trật tự, bảo vệ sinh cảnh quan - môi trường, nếp sống văn minh nơi công cộng, hoạt động xã hội,..", 2],
	"4": ["Có chứng nhận tham gia lớp bồi dưỡng nhận thức về Đảng từ mức Khá trở lên", 2],
	"5": ["Được kết nạp Đảng Cộng sản Việt Nam", 2],
	"6": ["Đạt danh hiệu Sinh viên năm tốt từ cấp Trường trở lên", 2],
	"7": ["Nhận bằng khen, huy chương tương đương cấp Bộ trở lên", 2],
}
tieuChiViPham = {
	"1": ["Bị cảnh cáo học tập mức 1", -4],
	"2": ["Bị cảnh cáo học tập mức 2", -6],
	"3": ["Bị cảnh cáo học tập mức 3", -8],
	"4": ["Vi phạm quy chế thi từ cảnh cáo trở lên", -6],
	"5": ["Bị kỷ luật khi thi hộ", -20],
	"6": ["Không hoàn thành học phí theo thời gian quy định", -4],
	"7": ["Vi phạm ở mức độ Khiển trách", -6],
	"8": ["Vi phạm ở mức độ Cảnh cáo", -9],
	"9": ["Vi phạm ở mức độ Kỷ luật buộc thôi học, tạm dừng", -12],
	"10": ["Không tham gia bất kỳ buổi SHCD nào do Nhà trường tổ chức", -5],
	"11": ["Không tham gia bất kỳ buổi SHCD nào do Viện tổ chức", -5],
	"12": ["Không tham gia bất kỳ buổi họp lớp nào do Lớp tổ chức", -5],
	"13": ["Vi phạm pháp luật thuộc nhóm tội danh hình sự", -50],
}
tieuChi2020 = {"hoctap": tieuChiHocTap, "kyluat": tieuChiKyLuat, "xahoi": tieuChiXaHoi,	"congdong": tieuChiCongDong, "vipham": tieuChiViPham}



print("{:^100}".format("KHUNG ĐIỂM ĐÁNH GIÁ KẾT QUẢ RÈN LUYỆN SINH VIÊN"))
print("{:^100}\n\n".format("NĂM HỌC 2019-2020"))

print("┌{:─^10}┬{:─^80}┬{:─^10}┐".format("─","─","─"))

print("│{:^10}│{:^80}│{:^10}│".format("STT","Tiêu chí đánh giá điểm rèn luyện","Điểm"))

for muc in tieuChi2020:
	print("├{:─^10}┼{:─^80}┼{:─^10}┤".format("─","─","─"))
	for tieuchi in tieuChi2020[muc]:
		print("│{:^10}│  {:<78}│{:^10}│".format(tieuchi, tieuChi2020[muc][tieuchi][0] if len(tieuChi2020[muc][tieuchi][0])<=76 else tieuChi2020[muc][tieuchi][0][:76], tieuChi2020[muc][tieuchi][1]))

print("└{:─^10}┴{:─^80}┴{:─^10}┘".format("─","─","─"))
os.system("pause")