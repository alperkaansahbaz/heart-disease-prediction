# Proje Yönetimi & GitHub Workflow

## 🌳 Branch Stratejisi (Git Flow - Sadeleştirilmiş)

```
main                    ← PRODUCTION (sadece stabil release'ler)
  └── develop           ← STAGING (aktif geliştirme)
       ├── feature/*    ← Yeni özellikler
       ├── bugfix/*     ← Hata düzeltmeleri
       └── docs/*       ← Sadece dokümantasyon
```

### Branch İsimlendirme Kuralları
```
feature/sprint1-eda-notebook
feature/sprint2-knn-model
feature/sprint4-flask-routing
bugfix/form-validation-empty-field
docs/update-readme
```

## 🔄 Development Workflow

### Adım 1: Yeni Task Başlatma
```bash
# develop'tan branch çıkar
git checkout develop
git pull origin develop
git checkout -b feature/sprint2-knn-model

# Çalış, commit'le
git add .
git commit -m "feat(model): KNN baseline model eğitimi eklendi"

# Push et
git push origin feature/sprint2-knn-model
```

### Adım 2: Pull Request (PR)
1. GitHub'da PR aç (`feature/...` → `develop`)
2. PR description doldur (template aşağıda)
3. Diğer ekip üyesine review ata
4. CI testleri yeşil olmalı
5. En az 1 onaydan sonra merge

### Adım 3: Sprint Sonu
`develop` → `main` merge edilir, tag atılır:
```bash
git tag -a v0.1.0-sprint1 -m "Sprint 1 tamamlandı"
git push origin v0.1.0-sprint1
```

---

## 📝 Commit Mesajı Standardı (Conventional Commits)

```
<tip>(<scope>): <kısa açıklama>

[opsiyonel detaylı açıklama]

[opsiyonel footer: Refs #issue-no]
```

### Tipler
| Tip | Kullanım | Örnek |
|-----|----------|-------|
| `feat` | Yeni özellik | `feat(model): XGBoost ensemble eklendi` |
| `fix` | Hata düzeltme | `fix(form): yaş alanı negatif değer hatası düzeltildi` |
| `docs` | Dokümantasyon | `docs(readme): kurulum adımları güncellendi` |
| `style` | Formatlama | `style(app): black formatter uygulandı` |
| `refactor` | Yeniden yapılandırma | `refactor(service): prediction service modülerleştirildi` |
| `test` | Test ekleme | `test(unit): validators için 5 test case eklendi` |
| `chore` | Bakım | `chore(deps): scikit-learn 1.5.2'ye yükseltildi` |
| `perf` | Performans | `perf(model): inference 2x hızlandı` |

### İyi Commit Örnekleri ✅
```
feat(eda): yaş ve kolesterol için 6 grafik eklendi
fix(predict): float dönüşüm hatası giderildi
docs(architecture): 3-tier diyagram güncellendi
test(integration): /predict endpoint için 4 senaryo eklendi
```

### Kötü Commit Örnekleri ❌
```
update                          ← belirsiz
fix bug                         ← hangi bug?
asdfasdf                        ← anlamsız
çalıştı sanırım                  ← profesyonel değil
```

---

## 🎫 Pull Request Template

PR açarken kullanılacak şablon. `.github/pull_request_template.md` olarak eklenecek.

```markdown
## 🎯 Açıklama
Bu PR ne yapıyor? Hangi sprint task'ına ait?

## 📋 Değişiklik Tipi
- [ ] 🆕 Yeni özellik (feature)
- [ ] 🐛 Hata düzeltme (bugfix)
- [ ] 📚 Dokümantasyon
- [ ] ♻️ Refactoring
- [ ] ✅ Test

## ✅ Checklist
- [ ] Kod local'de çalışıyor
- [ ] Yeni testler eklendi (gerekiyorsa)
- [ ] Mevcut testler geçiyor (`pytest`)
- [ ] Lint kontrolü yapıldı (`flake8`)
- [ ] README/docs güncellendi (gerekiyorsa)
- [ ] Conflict yok

## 📸 Ekran Görüntüleri (UI değişikliği varsa)
[ekran görüntüsü]

## 🔗 İlgili Issue
Closes #<issue-no>
```

---

## 🗂️ GitHub Issues / Trello Card Yapısı

### Trello Kullanırsanız:

**5 Liste Önerisi:**
1. 📌 **Backlog** — Tüm task'lar
2. 🎯 **Sprint Backlog** — Bu sprint'te yapılacaklar
3. 🚧 **In Progress** — Aktif çalışılanlar (max 2 adet/kişi)
4. 👀 **Review** — PR aşamasında olanlar
5. ✅ **Done** — Tamamlananlar

### Card Şablonu:
```
Başlık: [Sprint X] T2.4 — KNN Modeli Eğitimi

Açıklama:
Heart Disease dataset üzerinde KNN classifier eğit.
- k=5 ile başla
- 5-fold cross validation
- Accuracy, F1, ROC-AUC raporla

Acceptance Criteria:
- src/models/train_knn.py oluşturulmuş
- models/trained/knn_model.pkl kaydedildi
- Notebook'ta sonuçlar görselleştirilmiş

Tahmini süre: 4 saat
Atanan kişi: Alperen
Sprint: Sprint 2
Etiketler: ml, model-training
```

### GitHub Issues Kullanırsanız:

Issue açarken **Labels** kullanın:
- `sprint-1`, `sprint-2`, ..., `sprint-7`
- `priority:high`, `priority:medium`, `priority:low`
- `type:feature`, `type:bug`, `type:docs`
- `status:blocked`, `status:in-review`

**Milestones:** Her sprint için bir milestone oluşturun (örn: "Sprint 2 - Model Training").

**Projects (Beta):** GitHub Projects kanban board'u ile görsel takip yapın.

---

## 🤝 Code Review Kuralları

### Reviewer için Checklist
- [ ] Kod amacına uygun mu?
- [ ] Naming convention'a uyuluyor mu?
- [ ] Test var mı / coverage düştü mü?
- [ ] Magic number / hardcoded string var mı?
- [ ] Hata yönetimi (try/except) doğru mu?
- [ ] Yorumlar yeterli mi?
- [ ] Dökümantasyon güncellendi mi?

### Reviewer Tonu
- ❌ "Bu kod çok kötü"
- ✅ "Burada list comprehension kullanmak daha okunaklı olabilir, ne dersin?"

### Author için Kural
- PR'larınızı **küçük tut** (max 400 satır değişiklik)
- Conflict varsa **rebase** et (`git rebase develop`)
- Review geri bildirimini **savunmacı** değil, **öğrenme fırsatı** olarak gör

---

## 🚦 Definition of Done (Bitti Tanımı)

Bir task "Done" sayılması için:

- [x] Kod yazıldı
- [x] Local'de çalışıyor
- [x] Unit test eklendi (uygulanabilirse)
- [x] Code review onayı alındı
- [x] `develop` branch'ine merge edildi
- [x] Dokümantasyon güncellendi (gerekiyorsa)
- [x] Trello card / Issue kapatıldı

---

## 📅 Sprint Toplantı Şablonu

### Sprint Planning (Sprint başında, 1 saat)
1. Önceki sprint retrospektif sonuçlarını gözden geçir
2. Backlog'dan task'ları seç
3. Story point / saat tahmini yap
4. Görev dağılımı yap
5. Sprint hedefini yaz: "Bu sprint sonunda ___ tamamlanmış olacak"

### Daily Standup (Her gün, 15 dakika)
Üç soruya cevap:
1. Dün ne yaptım?
2. Bugün ne yapacağım?
3. Önümde engel var mı?

### Sprint Review (Sprint sonu, 30 dakika)
- Tamamlanan task'ları göster
- Demo yap
- Geri bildirim al

### Retrospective (Sprint sonu, 30 dakika)
Üç sütun:
- ✅ **Neyi iyi yaptık?**
- ❌ **Neyi kötü yaptık?**
- 💡 **Bir sonraki sprint'te ne deneyelim?**

---

## 🎓 Akademik Sunumda Bu Bölüm Nasıl Kullanılır?

Sunumda **"Proje Yönetimi"** slaydında şunları göster:

1. Trello/GitHub Projects kanban board ekran görüntüsü
2. Git commit history grafiği (`git log --graph --oneline`)
3. PR sayısı, kapatılan issue sayısı (GitHub Insights)
4. Sprint burndown chart (opsiyonel ama çok etkileyici)
5. Retrospektif notları (gerçek geri bildirimler)

> **Jüri tüyosu:** Mezuniyet projelerinde "Agile metodolojisi uyguladık" demek değil, **kanıtlamak** gerekir. Trello board'unun ekran görüntüsü, Git history, ve issue sayıları somut kanıttır.
