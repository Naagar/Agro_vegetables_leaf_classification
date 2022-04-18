data_transform_train = transforms.Compose([
                                        transforms.RandomRotation(30),
                                        transforms.RandomResizedCrop(224),
                                        transforms.RandomHorizontalFlip(),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

# Validation and Testing - just resize and crop the images
data_transform = transforms.Compose([
                                     transforms.Resize(255), 
                                     transforms.CenterCrop(224),
                                     transforms.ToTensor(),
                                     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
dataset = datasets.ImageFolder(data_dir, transform=data_transform_train)
train, val, test = torch.utils.data.random_split(dataset, [120,34])
trainLoader = torch.utils.data.DataLoader(train, batch_size=batch_size, 
                                           num_workers=num_workers, drop_last=True, shuffle=True)
valLoader = torch.utils.data.DataLoader(val, batch_size=batch_size, 
                                          num_workers=num_workers, drop_last=True)